import streamlit as st 
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Design the Page ... streamlit run app.py
st.title("Movie Recommender Systems")
user_input = st.text_input("Enter the Movie Title,genre or keyword")

