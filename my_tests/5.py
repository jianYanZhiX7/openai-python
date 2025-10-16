"""
该脚本演示如何使用 OpenAI Python SDK 的异步客户端（AsyncOpenAI）
向 Chat Completions 接口发送一条消息，并打印模型的回复。
"""

import asyncio  # asyncio：Python 原生异步框架，用于运行协程
from openai import DefaultAioHttpClient  # SDK 自带的默认异步 HTTP 客户端实现
from openai import AsyncOpenAI  # 异步版 OpenAI 客户端
import os  # 读取环境变量（如 BASE_URL、OPENAI_API_KEY）
from dotenv import load_dotenv  # 从 .env 文件加载环境变量

load_dotenv()  # 使 .env 中的配置可通过 os.environ 获取


async def main() -> None:
    # 创建并异步管理 OpenAI 客户端的生命周期
    async with AsyncOpenAI(
        base_url=os.environ.get("BASE_URL"),  # 自定义 API 网关或反向代理地址（未设置则使用官方默认）
        api_key=os.environ.get("OPENAI_API_KEY"),  # OpenAI API 密钥
        http_client=DefaultAioHttpClient(),  # 使用默认的 aiohttp 客户端
    ) as client:
        # 发送一次“聊天补全”请求，包含一条用户消息
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "说这是一个测试",  # 要求模型说“这是一个测试”
                }
            ],
            model="gpt-4o",  # 指定使用的模型
        )
        # 打印模型返回的第一条消息内容
        print(chat_completion.choices[0].message.content)


# 程序入口：启动事件循环并执行主协程
asyncio.run(main())
