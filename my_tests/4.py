import os
import asyncio
from my_client import aclient

# 异步使用

async def main() -> None:
    response = await aclient.responses.create(
        model="gpt-4o", input="向一个聪明五岁小孩解释反建制主义。"
    )
    print(response.output_text)


asyncio.run(main())

