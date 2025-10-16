import os
from openai import OpenAI
from openai import AsyncOpenAI

from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url=os.environ.get("BASE_URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)


aclient = AsyncOpenAI(
    base_url=os.environ.get("BASE_URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)