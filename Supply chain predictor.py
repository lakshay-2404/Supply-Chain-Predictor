# 01_Setup_and_Configuration.ipynb

# 1. Install Dependencies
pip install -q pandas openai crewai python-dotenv google-generativeai chromadb streamlit newsapi-python

# 2. Load API Keys
import os
from dotenv import load_dotenv
load_dotenv()

google_api_key = os.getenv("AIzaSyA2LH_6dHXmnINUr4R6RzkNPqLwikMiMGM")
news_api_key = os.getenv("b5fafddf536b4753a88dfca435432058")

# 3. Test Google Gemini Connection
import google.generativeai as genai
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Test connection: What is supply chain risk management?")
print("Gemini Connection Successful:", "supply chain risk management" in response.text.lower())