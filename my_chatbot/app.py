import streamlit as st
from groq import Groq

GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# page config - controls the browser tab title and layout
st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("Smith 🤖 - Your AI Assistant")
st.caption("Built with Groq + Streamlit - Week 1 project")

# System Prompt -  combines persona + confidence calibrartion
SYSTEM_PROMPT = """You are a helpful, honest AI Assistant named Smith with expertise in technology
and programming. Follow these rules:
1.Be concise - answer in 3-5 sentences unless the user asks for more detail.
2.If you are uncertain about a fact, say so briefly before answering.
3.For real-time data (prices, scores, current events), say you cannot provide reliable current information.
4.Be friendly but direct - no unnecessary filler phrases."""

# Session state stores the conversation history across reruns
# Without this, the page reloads and forgets everything on every message send
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# chat input at the bottom of the page
if user_input := st.chat_input("Ask me anything..."):

    #Add user message to history and display it immediately
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)


    # call Groq with full conversation history - this is how memory works
    # Every message in history gets sent back each time (context window in action )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": SYSTEM_PROMPT},
                  *st.session_state.messages # unpack full history here
        ],
        max_tokens = 500,

        temperature = 0.3       # factual default
    )

    assistant_reply = response.choices[0].message.content
    # Add reply to history and display it
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.write(assistant_reply)


    # Sidebar shows token awareness
    with st.sidebar:
        st.header("Session Info")
        st.metric("Messages so far", len(st.session_state.messages))
        total_chars = sum(len(m["content"]) for m in st.session_state.messages)
        st.metric("Approx chars in context", total_chars)
        st.caption("Context grows with every message — this is your context window filling up.")

        if st.button("Clear conversation"):
            st.session_state.messages = []
            st.rerun()
