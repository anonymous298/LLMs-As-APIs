import requests
import streamlit as st

def get_ollama_response(text_input):
    try:
        response = requests.post(
            'http://localhost:8000/essay/invoke',
            json={'input': {'topic': text_input}}
        )
        print("Raw Response from essay endpoint:", response.text)  # Debug: Print raw response
        return response.json()['output']
    except Exception as e:
        print("Error in get_ollama_response:", e)
        return None

def get_hugging_face_response(text_input):
    try:
        response = requests.post(
            'http://localhost:8000/question/invoke',
            json={'input': {'question': text_input}}
        )
        print("Raw Response from question endpoint:", response.text)  # Debug: Print raw response
        return response.json()['output']
    except Exception as e:
        print("Error in get_hugging_face_response:", e)
        return None

st.title('Langchain Demo With LLMs API')

input_text1 = st.text_input('Write an essay on ')
input_text2 = st.text_input('Ask a question about ')

if input_text1:
    response1 = get_ollama_response(input_text1)
    st.write(response1)

if input_text2:
    st.write(get_hugging_face_response(input_text2))