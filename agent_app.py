import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path

# Local .env loading
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

import google.generativeai as genai
import openai

# Load keys
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))

def run_gemini_agent():
    if not GEMINI_API_KEY:
        st.error("❌ GEMINI_API_KEY not found.")
        return
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    prompt = st.text_area("Enter your prompt for Gemini")
    if st.button("Run Gemini"):
        with st.spinner("Thinking with Gemini..."):
            response = model.generate_content(prompt)
            st.success("Response received:")
            st.write(response.text)

def run_openai_agent():
    if not OPENAI_API_KEY:
        st.error("❌ OPENAI_API_KEY not found.")
        return
    openai.api_key = OPENAI_API_KEY
    prompt = st.text_area("Enter your prompt for OpenAI")
    if st.button("Run OpenAI"):
        with st.spinner("Thinking with OpenAI..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.success("Response received:")
            st.write(response.choices[0].message.content)