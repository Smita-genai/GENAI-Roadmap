import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

st.set_page_config(page_title="Resume Optimizer", page_icon="📄", layout="wide")
st.title("📄 AI Resume Optimizer")
st.caption("Built with Groq + Streamlit — Week 2 Portfolio Project")

# --- Reusable LLM call — DRY principle ---
def llm_call(system: str, user: str, max_tokens: int = 600) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        max_tokens=max_tokens,
        temperature=0.2
    )
    return response.choices[0].message.content.strip()


# --- 3-step chain — defined ONCE, called ONCE ---
def run_resume_chain(resume_text: str, target_role: str) -> dict:
    """
    Each step feeds into the next.
    Spinners live here so UI feedback is part of the function,
    not duplicated outside it.
    """
    with st.spinner("Step 1/3 — Analysing weaknesses..."):
        weaknesses = llm_call(
            system=f"""You are a strict ATS expert and resume analyst for {target_role} roles 
            in the Indian IT industry. Identify ALL weaknesses in the resume.
            Output a numbered list only. No fixes yet. No preamble.
            Focus on: weak action verbs, missing metrics, ATS keywords missing 
            for {target_role}, vague descriptions, formatting issues.""",

            user=f"Analyse this resume:\n\n{resume_text}"
        )

    with st.spinner("Step 2/3 — Generating fixes..."):
        fixes = llm_call(
            system="""You are a resume improvement specialist.
            For each weakness, provide one specific actionable fix.
            Format strictly as:
            WEAKNESS: [weakness]
            FIX: [specific fix with rewritten text where relevant]---""",

            user=f"Generate fixes for:\n\n{weaknesses}"
        )

    with st.spinner("Step 3/3 — Rewriting resume..."):
        improved = llm_call(
            system=f"""You are a professional resume writer for Indian IT professionals 
            targeting {target_role} roles.
            CRITICAL: Never fabricate experience, metrics, or skills not in the original resume.
            If a point is vague and you cannot improve it without fabricating, 
            write: [NEEDS INPUT: ask user for specific detail here]
            Apply all fixes. Output the complete improved resume only. No commentary.""",
            
            user=f"Original:\n{resume_text}\n\nFixes:\n{fixes}",
            max_tokens=900
        )

    return {"weaknesses": weaknesses, "fixes": fixes, "improved": improved}


# --- LLM-as-judge evaluation ---
def evaluate_improvement(original: str, improved: str, target_role: str) -> str:
    return llm_call(
        system=f"""You are an objective resume evaluator for {target_role} roles.
        Score the improved resume vs original on three dimensions (1-5 each):
        - ATS Score: keyword density and formatting for ATS systems
        - Impact Language: strong action verbs and quantified achievements  
        - Clarity: clear, concise, easy to scan

        Output format:
        ATS Score: X/5 — [one sentence reason]
        Impact Language: X/5 — [one sentence reason]
        Clarity: X/5 — [one sentence reason]
        Overall: X/15
        Verdict: [one sentence — is this ready to submit?]""",

        user=f"Original:\n{original}\n\nImproved:\n{improved}"
    )


# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")
    target_role = st.selectbox(
        "Target Job Role",
        ["Python Developer", "AI/ML Engineer", "Data Engineer",
         "Data Analyst","DevOps Engineer","IT Support Specialist", "SAP Buisness Planning and Conslidation consultanat"]
    )
    st.divider()
    st.caption("Paste your resume in the main area and click Optimize.")
    st.caption("⚠️ Do not include personal contact details — "
               "this uses a free API and your data may be used for model training.")


# --- Main UI ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Resume")
    resume_input = st.text_area(
        "Paste your resume here",
        height=350,
        placeholder="Paste your resume text here...\n\nExample:\nSoftware Engineer at TechCorp (2022-2024)\n- Worked on backend systems\n- Helped with database tasks"
    )
    

with col2:
    st.subheader("Optimized Output")

    if st.button("🚀 Optimize Resume", type="primary", use_container_width=True):

        if not resume_input.strip():
            st.error("Please paste your resume text first.")
        else:
            # Call the function ONCE — clean, no duplication
            results = run_resume_chain(resume_input, target_role)

            # Display results in tabs
            tab1, tab2, tab3, tab4 = st.tabs(
                ["✅ Improved Resume", "🔍 Weaknesses", "🔧 Fixes", "📊 Eval Score"]
            )

            with tab1:
                st.text_area("Improved Resume", results["improved"],
                             height=300, key="improved_output")
                st.download_button(
                    "⬇️ Download Improved Resume",
                    results["improved"],
                    file_name="improved_resume.txt"
                )

            with tab2:
                st.markdown(results["weaknesses"])

            with tab3:
                st.markdown(results["fixes"])

            with tab4:
                with st.spinner("Running evaluation..."):
                    eval_score = evaluate_improvement(
                        resume_input, results["improved"], target_role
                    )
                st.markdown(eval_score)
                st.caption("Powered by LLM-as-judge")

            # Persist results across reruns
            st.session_state.last_results = results
