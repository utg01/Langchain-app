# Simple Health Chatbot (First Try)

This is a very basic chatbot built while learning LangChain for the first time. It uses a small Streamlit UI, a single prompt that asks the model to answer only health‑related queries, and routes requests through an OpenAI‑compatible endpoint. The goal was to get something minimal working end‑to‑end.

## What this is
- A beginner‑level Streamlit app that takes one text input and returns one text output.
- A single LangChain prompt and a simple chain: prompt → model → plain text parser.
- Model access is configured through an OpenAI‑compatible base URL and an API key in environment variables.

## Folder structure used
- app.py — the Streamlit page and LangChain logic.
- requirements.txt — minimal dependencies
- .env — local environment variables (not committed)
- README.md — this note

## Why it’s simple
- One system message acts as a “health prompt guard” to keep answers on topic. No tools, no memory, no retrieval
- One chain made with built‑in prompt template and a string output parser
- Environment is loaded with python‑dotenv and a couple of LangChain variables are set for basic project tagging

## Requirements
- Python installed
- An API key for the OpenAI‑compatible endpoint used by ChatOpenAI

## Setup steps I ran

```bash
# 1) Clone and enter
git clone https://github.com/utg01/Langchain-app
```


```bash
# 2) Create and activate a virtual environment
# macOS/Linux
python -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```


```bash
# 3) Install dependencies
pip install -r requirements.txt
```


```bash
# 4) Create a .env file in the project root (do not commit this)
# .env
OPENAI_API_KEY="your_api_key_here"
LANGCHAIN_PROJECT="my-demo-project"
LANGCHAIN_TRACING_V2="true"
```


```bash
# 5) Run the app
streamlit run app.py
```


Then open the local URL printed in the terminal to use the chatbot. It has one input box and shows the model’s reply below it

## How app.py is written (short)
- Loads .env, sets LANGCHAIN_PROJECT and LANGCHAIN_TRACING_V2, and builds a two‑message chat prompt.
- Uses ChatOpenAI with a base URL and model name that point to an OpenAI‑compatible provider; the key is read from OPENAI_API_KEY.
- Chains prompt → model → StrOutputParser, and on submit, displays the text result. That’s the entire flow.
  
## Notes I kept for myself
- For deployment, secrets can be moved from .env into a .streamlit/secrets.toml file or an app settings panel; both expose values to Streamlit at runtime.
- Keep .env and any secrets files out of Git; add them to .gitignore before pushing.

## What to try next (optional)
- Add basic error messages if the key is missing, and a small character limit for inputs.[1]
- Swap the model name or temperature in the ChatOpenAI init to see different response styles.[3]

