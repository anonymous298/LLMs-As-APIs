from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_huggingface import HuggingFaceEndpoint
from langserve import add_routes
import os
import uvicorn

app = FastAPI(
    title='Langchain Server',
    version='1.0',
    description='A Simple API Server Containing LLMs'
)

llm_ollama = Ollama(model='deepseek-r1:1.5b')
llm_hf = HuggingFaceEndpoint(repo_id='mistralai/Mistral-7B-Instruct-v0.3', token=os.getenv('HUGGING_FACE_API'), temperature=0.5)

prompt1 = ChatPromptTemplate.from_template('Write me an essay about {topic}')
prompt2 = ChatPromptTemplate.from_template('Answer me this question: {question} in simple words')

add_routes(
    app,
    prompt1 | llm_ollama | StrOutputParser(),
    path='/essay'
)

add_routes(
    app,
    prompt2 | llm_hf | StrOutputParser(),
    path='/question'
)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)