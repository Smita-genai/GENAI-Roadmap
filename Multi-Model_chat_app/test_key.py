import os
from dotenv import load_dotenv
load_dotenv()
print("Groq Key present:", bool(os.getenv("GROQ_API_KEY")))
print("OpenRouter Key present:", bool(os.getenv("OPENROUTER_API_KEY")))