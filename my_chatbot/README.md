# AI Chatbot with Memory

A conversational AI assistant built with Groq (Llama 3.3 70B) and Streamlit.

## Live Demo
[Click here to try it](https://genai-roadmap-emzwstxqts7app2nux4lt5h.streamlit.app)

## What it does
- Multi-turn conversation with full memory (context window in action)
- Custom persona and confidence-calibration system prompt
- Real-time context size tracking in the sidebar
- Clear conversation button to reset session

## Tech Stack
- Groq API (Llama 3.3 70B)
- Streamlit
- python-dotenv

## Run locally
pip install streamlit groq python-dotenv
# Add your GROQ_API_KEY to .env
streamlit run app.py