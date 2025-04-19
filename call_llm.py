import os
import google.generativeai as genai
import openai

def run_gemini_agent(prompt: str, api_key: str, model_name: str = "gemini-1.5-pro-latest") -> str:
    """
    Calls the Gemini API with a given prompt and API key.
    Returns the plain text response.
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text

def run_openai_agent(prompt: str, api_key: str, model_name: str = "gpt-3.5-turbo") -> str:
    """
    Calls the OpenAI API with a given prompt and API key.
    Returns the plain text response.
    """
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
