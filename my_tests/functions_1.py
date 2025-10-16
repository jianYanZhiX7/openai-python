from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    base_url=os.environ.get("BASE_URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA",
              },
              "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
          },
          "required": ["location", "unit"],
        }
    }
]

response = client.responses.create(
  model="gpt-5",
  tools=tools,
  input="北京今天天气怎么样",
  tool_choice="auto"
)

print(response)
