import asyncio

from my_client import aclient


# 异步客户端  流模式

async def main():
    stream = await aclient.responses.create(
        model="gpt-4o",
        input="写一个关于独角兽的一句话睡前故事。不少于300字",
        stream=True,
    )

    async for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end='')


asyncio.run(main())