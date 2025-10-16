from my_client import client

stream = client.responses.create(
    model="gpt-4o",
    input="写一个关于独角兽的一句话睡前故事。不少于300字",
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end='')