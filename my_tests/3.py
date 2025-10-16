import base64
from my_client import client

# 图片识别

# 使用 base64 编码的图像字符串：
prompt = "这张图片里有什么？"
with open("image.png", "rb") as image_file:
    b64_image = base64.b64encode(image_file.read()).decode("utf-8")

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": f"data:image/png;base64,{b64_image}"},
            ],
        }
    ],
)

print(response.output_text)
# 这张图片中有一只浣熊，正在一个树的边缘探出头来。树的表面纹理清晰，周围环境较为阴暗。浣熊的毛发颜色和面部特征很明显。
