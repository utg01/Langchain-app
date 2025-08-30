Below is a tailored, production‑ready README for the exact file structure and code shown, with big headings and bash‑formatted commands. It uses OpenRouter via ChatOpenAI, Streamlit, and dotenv, and recommends Streamlit secrets for deployment.

# LangChain Health Q&A (OpenRouter + Streamlit)[1][2][3]

A minimal health‑focused Q&A app built with Streamlit and LangChain’s ChatOpenAI, routing to Gemini through OpenRouter’s API. Only health‑related answers are produced via a strict system prompt.[2][3][1]

## Features[3][1]
- Uses ChatOpenAI with base_url to call Gemini on OpenRouter, so existing OpenAI tooling works out of the box.[2][3]
- Health‑only responses enforced by a system prompt and simple LangChain chain.[1][3]
- Local .env support via python‑dotenv and optional Streamlit secrets for safe deployments.[4][5]

## Project Structure[5][4]
- app.py — Streamlit UI, LangChain prompt, and ChatOpenAI configured for OpenRouter.[3][1]
- requirements.txt — Dependencies for Streamlit, LangChain, and langchain-openai.[1][3]
- .env — Local environment variables for development; never commit to Git.[4][5]
- README.md — Documentation.[5][4]

## Prerequisites[2][3]
- Python 3.10+ recommended.[3]
- OpenRouter API key from the OpenRouter dashboard.[2]
- A model available on OpenRouter, e.g., google/gemini-2.5-flash. Use the provider’s canonical name as model.[2]

## Quick Start[1][2]

### 1) Clone the repo[1]
```bash
git clone https://github.com/utg01/langchain-health-demo.git
cd langchain-health-demo
```

### 2) Create and activate a virtualenv[1]
```bash
# macOS/Linux
python -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3) Install dependencies[3][1]
```bash
pip install -r requirements.txt
# If needed explicitly:
pip install -U langchain-openai python-dotenv streamlit
```

### 4) Configure environment variables (local)[4][5]
Option A — .env (used by python‑dotenv):[5][4]
```bash
# .env
OPENAI_API_KEY="your_openrouter_api_key"  # OpenRouter key
LANGCHAIN_PROJECT="my-demo-project"
LANGCHAIN_TRACING_V2="true"
```
The code reads OPENAI_API_KEY and points ChatOpenAI to base_url=https://openrouter.ai/api/v1.[3][2]

Option B — Streamlit secrets for local and cloud: create .streamlit/secrets.toml and access with st.secrets.[4][5]
```toml
# .streamlit/secrets.toml
OPENAI_API_KEY = "your_openrouter_api_key"
LANGCHAIN_PROJECT = "my-demo-project"
LANGCHAIN_TRACING_V2 = "true"
```
In app.py, either rely on dotenv or use st.secrets["OPENAI_API_KEY"]. Both are supported by Streamlit.[5][4]

### 5) Run the app[4]
```bash
streamlit run app.py
```
Open http://localhost:8501 to interact with the assistant.[4]

## How It Works (app.py)[3][1]
- Loads .env with load_dotenv, sets LangChain project and tracing flags.[1][3]
- Defines a ChatPromptTemplate with a system message restricting output to health content.[1]
- Configures ChatOpenAI with base_url=https://openrouter.ai/api/v1, model="google/gemini-2.5-flash", and api_key from OPENAI_API_KEY (OpenRouter key).[2][3]
- Streams user input through prompt → llm → StrOutputParser and renders in Streamlit.[3][1]

Tip: Some OpenRouter integrations expect model_name instead of model; ChatOpenAI accepts model or model_name and respects base_url. If an SDK mismatch occurs, pass model_name explicitly.[6][3]

## Environment & Keys Guidance[5][2]
- OPENAI_API_KEY is used intentionally for OpenRouter because ChatOpenAI reads this variable by default; base_url switches the backend to OpenRouter. This is the standard approach in LangChain OpenAI clients.[2][3]
- Never commit .env or secrets; rely on Streamlit’s secrets or deployment environment variables.[5][4]

## Deploy to Streamlit Community Cloud[4][5]
- Push the repo to GitHub and connect it in Streamlit Community Cloud.[5][4]
- App Settings → Secrets (TOML format):[4][5]
```toml
OPENAI_API_KEY = "your_openrouter_api_key"
LANGCHAIN_PROJECT = "my-demo-project"
LANGCHAIN_TRACING_V2 = "true"
```
In code, read from st.secrets or environment as preferred; Streamlit injects both.[5][4]

## Troubleshooting[7][3]
- 401/403 errors: verify OPENAI_API_KEY is an OpenRouter key and base_url is https://openrouter.ai/api/v1.[2][3]
- Model errors: ensure the model slug matches OpenRouter’s catalog, e.g., google/gemini-2.5-flash; some features like tools may have differences across providers.[7][2]
- If the client insists on OPENROUTER_API_KEY naming, subclassing or setting env mapping is a common workaround, but base_url + OPENAI_API_KEY works for ChatOpenAI in current LangChain.[7][3]

## Security Notes[4][5]
- Use .streamlit/secrets.toml locally and in cloud deployments; Streamlit maps them to st.secrets and environment variables at runtime.[5][4]
- Keep .env and secrets files out of version control and never paste keys in PRs/issues.[4][5]

## License[1]
MIT, as in the original project description.[1]

[1](https://python.langchain.com/docs/integrations/chat/openai/)
[2](https://openrouter.ai/docs/quickstart)
[3](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)
[4](https://docs.streamlit.io/develop/api-reference/connections/st.secrets)
[5](https://docs.streamlit.io/develop/concepts/connections/secrets-management)
[6](https://huggingface.co/spaces/barunsaha/slide-deck-ai/commit/3b3664d085ad1c8a5553f163bdabe84e70c6e09d)
[7](https://github.com/langchain-ai/langchain/discussions/27964)
[8](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/84015689/8e193aa8-0be4-4b8c-a840-41247d895cc5/image.jpg?AWSAccessKeyId=ASIA2F3EMEYE3NQMSEW2&Signature=WY7fAZHXtt%2F7zf%2F6osb43wBiefo%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIHm6upU1V6zj5Ka6t%2FOFtUedrMWOPWJJEki%2FOBkx2MwAAiAV%2BUtAUZUSDy24xB9UjTUjpsp6wz4ZPjavo5Gf0XJUbir6BAjg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMxTenPvmw579THs%2F3Ks4EqnlFgtKAl0OJbfcNa0gVNqK4A6Q%2F4NApylJoSmaWLF3VShf8iDAHGgm6bueZzHYTcJt0Agq6krLpv30ahv2WDXA6Nnb6nrQwlXqDdfR%2Bi5pOVkf0H6hCBwF%2BH0v2PwyfSby8mjO7O9xpV0xM9CMV8iL%2F5llau3RM3dxbxu60UQHNjgFGkAT4GCXp1YuBXUKcytqLocGh%2BIUWEF0c0EnvUvinAkGf8aRkOFfTkR7huTSCu9jIflnTtMqP8tmkM8lRamONl7Ejp%2BndEoJdpfC%2BMDkDQmfLScwRI3S4fHU%2BGrFjM5icLQ5AiQJUJkZ13TYiH0QMywFPQt5v6ckfwFRpClKmgudoQ9Jz8EaxLqqxO4FdbPRK8i5yNCCwrOt%2BQrmdqux%2FrYJpaAtP35FW8%2BSAnDziCNnEbbFUPuP3fo%2FqosztIF5jUpUdXjMbcqF%2FiiQi29VvuHf5Jm%2BG0DrnkxE7ntJGBoh8rQN9UPjEUiFN57snNwzs9pkPRx2yhx2msqtBoHOyjLUmCcbvACFvN5MyDs9R2bOvLjr2D9PYUp11A2AAasshxIZKv%2BtFmuqvut3upsLJZZKaGOGPa5Qi4NGIAZ8Bp%2BS5hogP%2FJOdUdiPNnJRTWwsEW5diI3GjN8WRbvqlxSevBubfJR8Gkq0PZZBOE13JlB5294HF9z0p46C53c9Y7%2FgmgsJHkvzOQb0FpB5rKJczxOXjw7w8c2q43ZNsQfMojd2abRBrLxUErG7IeMqrTTjazc3GkWoxC71IkE1NqcnqCMhhxpcqlMmjwMwlIHOxQY6mwHqqrkq%2FQ44geSSq9lS42yQou2KJfBbHqFSXElmQYfuzn6PMXT%2Be2QgwgUnkfDWYe1WY5hG0Mq7grHAlB4z0c600cUaG5hEgZR4gawrOLzB0L%2FbUOzTe78X78YZZj2g9PLb9ZbW5qx75KrKVLFgNzPmGVspXGczOUwW%2FhAUCqoJCed2Z%2FgsmnAJbdPuyJsSEylJqfUUlrou5wlsMA%3D%3D&Expires=1756596137)
[9](https://openrouter.ai/docs/community/lang-chain)
[10](https://www.datasciencebyexample.com/2023/12/27/enable-secrets-in-using-streamlit-app/)
[11](https://blog.gopenai.com/from-curiosity-to-code-my-journey-into-ai-agents-with-langchain-and-openrouter-2c10ae5d2aff)
[12](https://github.com/langchain-ai/langchain/issues/31325)
[13](https://gist.github.com/rbiswasfc/f38ea50e1fa12058645e6077101d55bb)
