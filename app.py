from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os 
from dotenv import load_dotenv 
os.environ["LANGCHAIN_PROJECT"] = "my-demo-project"
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


## PROMPT TEMPELATE

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant, please respond with refferance to health only"),
        ("user","Question:{question}")
    ]
)

## STREAMLIT FRAMEWORK
st.title("Langchain Demo with gemini api")
input_text=st.text_input("Search the question you want:")


## gen ai llm
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash")
output_parser=StrOutputParser()
chain=prompt| llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
