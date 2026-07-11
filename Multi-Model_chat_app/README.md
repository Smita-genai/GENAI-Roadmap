# Multi-Model Chat

A Streamlit chat app that lets you switch between multiple free LLM providers 
(Groq, OpenRouter) mid-conversation, with chat history and error handling.

## Live Demo
[https://genai-roadmap-ja6oz89wbgad6bq8vjffff.streamlit.app]

## Features
- Dropdown to switch between models (Groq Llama 3.3 70B, OpenRouter free models)
- Persistent chat history using Streamlit session state
- Error handling for empty messages and failed API calls
- Loading spinner while waiting for responses

## Tech Stack
- Python
- Streamlit
- Groq API
- OpenRouter API
- python-dotenv

## Run Locally
1. Clone this repo
2. `pip install -r requirements.txt`
3. Create a `.env` file with:
GROQ_API_KEY=your_key_here
OPENROUTER_API_KEY=your_key_here
4. `streamlit run app.py`


## What I Learned
Built as part of a self-directed Generative AI development path — practiced 
multi-provider API integration, Streamlit session state management, and 
debugging real API errors (auth issues, environment variable handling).