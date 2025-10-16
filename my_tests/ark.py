import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url=os.environ.get("BASE_URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)

model = os.environ.get("MODEL")
if not model:
    raise ValueError("MODEL environment variable is not set")

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "你是人工智能助手"},
        {"role": "user", "content": "你好"},
    ],
)
print(completion.choices[0].message.content)

# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "你是人工智能助手"},
        {"role": "user", "content": "什么是人工智能"},
    ],
    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue
    print(chunk.choices[0].delta.content, end="")
print()
