import os

import requests
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from model_config import MODELS

load_dotenv()

st.set_page_config(page_title="Multi-Model Chat", page_icon="💬")
st.title("Multi-Model Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

selected = st.selectbox("Choose a model", list(MODELS.keys()))

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant":
            st.caption(f"*{msg['model']}*")
        st.write(msg["content"])

if prompt := st.chat_input("Type a message..."):
    if not prompt.strip():
        st.warning("Please enter a message.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        cfg = MODELS[selected]
        api_messages = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]

        with st.spinner("Thinking..."):
            try:
                if cfg["provider"] == "groq":
                    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
                    resp = client.chat.completions.create(
                        model=cfg["model_name"],
                        messages=api_messages,
                        max_tokens=500,
                    )
                    reply = resp.choices[0].message.content
                else:
                    key = os.getenv("OPENROUTER_API_KEY")
                    r = requests.post(
                        "https://openrouter.ai/api/v1/chat/completions",
                        headers={"Authorization": f"Bearer {key}"},
                        json={"model": cfg["model_name"], "messages": api_messages},
                        timeout=60,
                    )
                    r.raise_for_status()
                    reply = r.json()["choices"][0]["message"]["content"]

                st.session_state.messages.append(
                    {"role": "assistant", "content": reply, "model": selected}
                )
                with st.chat_message("assistant"):
                    st.caption(f"*{selected}*")
                    st.write(reply)

            except Exception as e:
                st.error(f"Something went wrong: {e}")