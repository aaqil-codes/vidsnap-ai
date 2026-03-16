import os
from dotenv import load_dotenv

# load variables from .env file
load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")