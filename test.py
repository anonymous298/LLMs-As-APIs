import streamlit as st
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Streamlit Title
st.title('Chatbot Using Langchain And HuggingFace API')

# Hugging Face API details
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
sec_key = os.getenv('HUGGING_FACE_API')

# Initialize HuggingFace LLM correctly
llm = HuggingFaceEndpoint(
    repo_id=repo_id, 
    huggingfacehub_api_token=sec_key,  # ✅ Correct API token parameter
    task="text-generation",            # ✅ Explicit task for text models
    temperature=0.3,  # ✅ Pass directly
)

# Input Text Field
input_text = st.text_input('What do you want to ask? ')

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are an Intelligent Assistant'),
    ('user', 'Answer this question: {question} in short and simple words')
])

# LangChain Pipeline
chain = prompt | llm | StrOutputParser()

# Streamlit Button to Generate Response
if st.button('Ask'):
    response = chain.invoke({'question': input_text})
    st.write(response)
