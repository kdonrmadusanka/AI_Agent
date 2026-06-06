import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file into environment variables

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REDIS_URL = os.getenv("REDIS_URL")

# Optional safety check
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in .env")