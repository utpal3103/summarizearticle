import streamlit as st
from agent_app import run_openai_agent, run_gemini_agent

st.title("🔧 Agent Selector")

agent_choice = st.radio("Choose your backend:", ["OpenAI", "Gemini"])

if agent_choice == "OpenAI":
    run_openai_agent()
elif agent_choice == "Gemini":
    run_gemini_agent()