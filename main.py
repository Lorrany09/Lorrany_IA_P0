import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

MODELO = "models/gemini-3.1-flash-lite"

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))