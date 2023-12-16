import os
from pathlib import Path
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

speech_file_path = Path(__file__).parent / "ImranSarwarSpeech.mp3"

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hi i am Imran Sarwar.Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)
