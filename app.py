from dotenv import load_dotenv
load_dotenv() #loading env variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

##function to load geminin pro and get resposes
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A Demo")

st.header("MedMasters")

input = st.text_input("Input: ",key = "input")

submit = st.button("Ask question")

if submit:
    response = get_gemini_response(input)
    st.write(response)
   
