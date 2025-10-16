"""
结构化输出
https://platform.openai.com/docs/guides/structured-outputs
"""

from my_client import client
from rich import print
from pydantic import BaseModel

class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

response = client.chat.completions.parse(
   messages=[
        {"role": "system", "content": "Guide the user through the solution step by step."},
        {"role": "user", "content": "github上某个仓库存在错误,我修复了,如何能让他合并到主分支"}
    ],
    response_format=MathReasoning,
    model="gpt-5",
)

math_reasoning = response.choices[0].message

# If the model refuses to respond, you will get a refusal message

if (math_reasoning.refusal):
    print(math_reasoning.refusal)
else:
    print(math_reasoning.parsed)