import requests
import streamlit as st


def get_result(input_text):
    
    response = requests.post(
        "http://localhost:8000/analysis/invoke",
        json={'input': input_text}
    ) 
    
    print(f"Response success: {response}")
    
    return response.json()['output']

st.title("Survey Data Analysis")
input_text = st.text_input("Ask question here!!")

if input_text:
    st.write(get_result(input_text=input_text))