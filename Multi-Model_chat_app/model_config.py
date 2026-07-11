# model_config.py
# Purpose: single source of truth for which providers/models
# your multi-model chat app can use. Tomorrow's app will import this.

MODELS = {
    "Groq - Llama 3.3 70B": {
        "provider": "groq",
        "model_name": "llama-3.3-70b-versatile",
    },
    "Groq - Qwen Vision": {
        "provider": "groq",
        "model_name": "qwen/qwen3.6-27b",
    },
    # add an OpenRouter entry once you've got a key from openrouter.ai
    "OpenRouter - Free": {
        "provider": "openrouter",
        "model_name": "openrouter/free",
    },
}

# quick sanity print — confirms the dict loads correctly
if __name__ == "__main__":
    for label, cfg in MODELS.items():
        print(f"{label}: provider={cfg['provider']}, model={cfg['model_name']}")