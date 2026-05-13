import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

MODEL_NAME = "openai/gpt-3.5-turbo"

CHROMA_DIR = "../chroma_db"
PDF_DIR = "../../data/pdfs"