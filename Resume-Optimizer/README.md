# AI Resume Optimizer

An AI-powered resume optimizer for Indian IT professionals, 
built with a 3-step prompt chain and LLM-as-judge evaluation.

## Live Demo
[Try it here](YOUR_STREAMLIT_URL)

## How it works
1. **Analyse** — identifies ATS weaknesses and missing keywords
2. **Fix** — generates specific improvements for each weakness  
3. **Rewrite** — produces an improved resume applying all fixes
4. **Evaluate** — scores the improvement using LLM-as-judge

## Tech Stack
- Groq API (Llama 3.3 70B)
- Streamlit
- Prompt chaining (3-step pipeline)
- LLM-as-judge evaluation

## Prompt Engineering techniques used
- Role prompting, structured prompts, prompt chaining, 
  CoT reasoning, LLM-as-judge evaluation

## Run locally
pip install streamlit groq python-dotenv
# Add GROQ_API_KEY to .env
streamlit run app.py
