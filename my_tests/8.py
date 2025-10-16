import asyncio
from openai import AsyncOpenAI
from my_client import aclient

async def main():
    manager = aclient.realtime.connect(model="gpt-realtime")
    base_ws_url = manager._prepare_url()
    ws_url = base_ws_url.copy_with(params={**dict(aclient.base_url.params), "model": "gpt-realtime"})
    print(f"WebSocket URL: {ws_url}")
    async with manager as connection:
        await connection.session.update(session={'modalities': ['text']})

        await connection.conversation.item.create(
            item={
                "type": "message",
                "role": "user",
                "content": [{"type": "input_text", "text": "打个招呼！"}],
            }
        )
        await connection.response.create()

        async for event in connection:
            if event.type == 'response.text.delta':
                print(event.delta, flush=True, end="")

            elif event.type == 'response.text.done':
                print()

            elif event.type == "response.done":
                break

asyncio.run(main())