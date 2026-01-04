import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env

api_key = os.getenv('OPENAI_API_KEY')

print("The OpenAI API key is:", api_key)
