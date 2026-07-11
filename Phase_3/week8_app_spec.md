# Multi-Model Streamlit Chat App — Spec

## Must have
- Dropdown to pick model (from model_config.py MODELS dict)
- Text input box for user message
- Chat history displayed, persisted across turns (st.session_state)
- Shows which model answered each message

## Nice to have (only if time allows)
- Token/cost estimate shown per response
- Clear chat button

## Explicitly NOT doing
- No Gemini entry unless quota allows that day
- No authentication/login
- No image upload yet (that's a separate Week 7-8 project)