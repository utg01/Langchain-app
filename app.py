from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os 
from dotenv import load_dotenv 

# Load .env file
load_dotenv()

# LangChain project settings
os.environ["LANGCHAIN_PROJECT"] = "my-demo-project"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## PROMPT TEMPLATE
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, please respond with reference to health only"),
        ("user", "Question: {question}")
    ]
)

## STREAMLIT UI
st.title("LangChain Demo with Gemini API (via OpenRouter)")
input_text = st.text_input("Search the question you want:")

## LLM setup with OpenRouter Gemini
llm = ChatOpenAI(
    model="google/gemini-2.5-flash",   # ✅ Gemini via OpenRouter
    api_key=os.getenv("OPENAI_API_KEY"),  # ✅ OpenRouter key goes here
    base_url="https://openrouter.ai/api/v1",
    max_completion_tokens=512
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
