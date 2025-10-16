import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url=os.environ.get("BASE_URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-5",
    instructions="你是一个像海盗一样说话的编程助手。",
    input="如何检查 Python 对象是否是某个类的实例？",
)

print(response.output_text)
