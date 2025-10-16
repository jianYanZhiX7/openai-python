# OpenAI Python API 库

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/openai.svg?label=pypi%20(stable))](https://pypi.org/project/openai/)

OpenAI Python 库为任何 Python 3.8+ 应用程序提供了便捷的 OpenAI REST API 访问方式。该库包含所有请求参数和响应字段的类型定义，并提供由 [httpx](https://github.com/encode/httpx) 驱动的同步和异步客户端。

它是使用 [Stainless](https://stainlessapi.com/) 从我们的 [OpenAPI 规范](https://github.com/openai/openai-openapi) 生成的。

## 文档

REST API 文档可以在 [platform.openai.com](https://platform.openai.com/docs/api-reference) 上找到。本库的完整 API 文档请参见 [api.md](api.md)。

## 安装

```sh
# 从 PyPI 安装
pip install openai
```

## 使用方法

本库的完整 API 文档请参见 [api.md](api.md)。

与 OpenAI 模型交互的主要 API 是 [Responses API](https://platform.openai.com/docs/api-reference/responses)。您可以使用以下代码从模型生成文本：

```python
import os
from openai import OpenAI

client = OpenAI(
    # 这是默认值，可以省略
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-4o",
    instructions="你是一个像海盗一样说话的编程助手。",
    input="如何检查 Python 对象是否是某个类的实例？",
)

print(response.output_text)
```

之前用于生成文本的标准（无限期支持）是 [Chat Completions API](https://platform.openai.com/docs/api-reference/chat)。您可以使用该 API 通过以下代码从模型生成文本：

```python
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "像海盗一样说话。"},
        {
            "role": "user",
            "content": "如何检查 Python 对象是否是某个类的实例？",
        },
    ],
)

print(completion.choices[0].message.content)
```

虽然您可以提供 `api_key` 关键字参数，
但我们推荐使用 [python-dotenv](https://pypi.org/project/python-dotenv/)
将 `OPENAI_API_KEY="My API Key"` 添加到您的 `.env` 文件中，
这样您的 API 密钥就不会存储在源代码控制中。
[在此获取 API 密钥](https://platform.openai.com/settings/organization/api-keys)。

### 视觉功能

使用图像 URL：

```python
prompt = "这张图片里有什么？"
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/2023_06_08_Raccoon1.jpg/1599px-2023_06_08_Raccoon1.jpg"

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": f"{img_url}"},
            ],
        }
    ],
)
```

使用 base64 编码的图像字符串：

```python
import base64
from openai import OpenAI

client = OpenAI()

prompt = "这张图片里有什么？"
with open("path/to/image.png", "rb") as image_file:
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
```

## 异步使用

只需导入 `AsyncOpenAI` 而不是 `OpenAI`，并在每个 API 调用中使用 `await`：

```python
import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    # 这是默认值，可以省略
    api_key=os.environ.get("OPENAI_API_KEY"),
)


async def main() -> None:
    response = await client.responses.create(
        model="gpt-4o", input="向一个聪明五岁小孩解释反建制主义。"
    )
    print(response.output_text)


asyncio.run(main())
```

同步和异步客户端之间的功能完全相同。

### 使用 aiohttp

默认情况下，异步客户端使用 `httpx` 进行 HTTP 请求。然而，为了获得更好的并发性能，您也可以使用 `aiohttp` 作为 HTTP 后端。

您可以通过安装 `aiohttp` 来启用此功能：

```sh
# 从 PyPI 安装
pip install openai[aiohttp]
```

然后您可以通过实例化客户端并设置 `http_client=DefaultAioHttpClient()` 来启用它：

```python
import asyncio
from openai import DefaultAioHttpClient
from openai import AsyncOpenAI


async def main() -> None:
    async with AsyncOpenAI(
        api_key="My API Key",
        http_client=DefaultAioHttpClient(),
    ) as client:
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "说这是一个测试",
                }
            ],
            model="gpt-4o",
        )


asyncio.run(main())
```

## 流式响应

我们提供使用服务器发送事件（SSE）的流式响应支持。

```python
from openai import OpenAI

client = OpenAI()

stream = client.responses.create(
    model="gpt-4o",
    input="写一个关于独角兽的一句话睡前故事。",
    stream=True,
)

for event in stream:
    print(event)
```

异步客户端使用完全相同的接口。

```python
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()


async def main():
    stream = await client.responses.create(
        model="gpt-4o",
        input="写一个关于独角兽的一句话睡前故事。",
        stream=True,
    )

    async for event in stream:
        print(event)


asyncio.run(main())
```

## Realtime API

Realtime API 使您能够构建低延迟、多模态对话体验。它目前支持文本和音频作为输入和输出，以及通过 WebSocket 连接进行 [函数调用](https://platform.openai.com/docs/guides/function-calling)。

在底层，SDK 使用 [`websockets`](https://websockets.readthedocs.io/en/stable/) 库来管理连接。

Realtime API 通过客户端发送事件和服务器发送事件的组合来工作。客户端可以发送事件来执行诸如更新会话配置或发送文本和音频输入等操作。服务器事件确认音频响应何时完成，或者何时收到模型的文本响应。完整的事件参考可以在[这里](https://platform.openai.com/docs/api-reference/realtime-client-events)找到，指南可以在[这里](https://platform.openai.com/docs/guides/realtime)找到。

基本文本示例：

pip install openai[realtime]

```py
import asyncio
from openai import AsyncOpenAI

async def main():
    client = AsyncOpenAI()

    async with client.realtime.connect(model="gpt-realtime") as connection:
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
```

然而，Realtime API 的真正魅力在于处理音频输入/输出，请参见这个示例 [TUI 脚本](https://github.com/openai/openai-python/blob/main/examples/realtime/push_to_talk_app.py) 以获取完整示例。

### Realtime 错误处理

每当发生错误时，Realtime API 将发送一个 [`error` 事件](https://platform.openai.com/docs/guides/realtime-model-capabilities#error-handling)，连接将保持打开并仍然可用。这意味着您需要自己处理它，因为当 `error` 事件传入时，SDK _不会直接引发任何错误_。

```py
client = AsyncOpenAI()

async with client.realtime.connect(model="gpt-realtime") as connection:
    ...
    async for event in connection:
        if event.type == 'error':
            print(event.error.type)
            print(event.error.code)
            print(event.error.event_id)
            print(event.error.message)
```

## 使用类型

嵌套请求参数是 [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict)。响应是 [Pydantic 模型](https://docs.pydantic.dev)，它们还提供了诸如以下内容的辅助方法：

- 序列化回 JSON，`model.to_json()`
- 转换为字典，`model.to_dict()`

类型化的请求和响应在您的编辑器中提供自动完成和文档。如果您希望在 VS Code 中更早地看到类型错误以帮助捕获错误，请将 `python.analysis.typeCheckingMode` 设置为 `basic`。

## 获取微调模型



 通过 OpenAI API 获取当前账号下所有 fine-tuning（微调训练）任务的列表，并打印出来。 



```python
from openai import OpenAI

client = OpenAI()

all_jobs = []
# 根据需要自动获取更多页面。
for job in client.fine_tuning.jobs.list(
    limit=20,
):
    # 在这里对 job 执行某些操作
    all_jobs.append(job)
print(all_jobs)
```

或者，异步方式：

```python
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()


async def main() -> None:
    all_jobs = []
    # 遍历所有页面中的项目，根据需要发出请求。
    async for job in client.fine_tuning.jobs.list(
        limit=20,
    ):
        all_jobs.append(job)
    print(all_jobs)


asyncio.run(main())
```

或者，您可以使用 `.has_next_page()`、`.next_page_info()` 或 `.get_next_page()` 方法来更精细地控制分页：

```python
first_page = await client.fine_tuning.jobs.list(
    limit=20,
)
if first_page.has_next_page():
    print(f"将使用这些详细信息获取下一页: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"我们刚刚获取的项目数量: {len(next_page.data)}")

# 对于非异步用法，请删除 `await`。
```

或者直接使用返回的数据：

```python
first_page = await client.fine_tuning.jobs.list(
    limit=20,
)

print(f"下一页游标: {first_page.after}")  # => "下一页游标: ..."
for job in first_page.data:
    print(job.id)

# 对于非异步用法，请删除 `await`。
```

## 嵌套参数

嵌套参数是字典，使用 `TypedDict` 进行类型化，例如：

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.responses.create(
    input=[
        {
            "role": "user",
            "content": "多少钱？",
        }
    ],
    model="gpt-4o",
    response_format={"type": "json_object"},
)
```

## 文件上传

对应于文件上传的请求参数可以作为 `bytes` 传递，或者作为 [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) 实例或 `(filename, contents, media type)` 元组传递。

```python
from pathlib import Path
from openai import OpenAI

client = OpenAI()

client.files.create(
    file=Path("input.jsonl"),
    purpose="fine-tune",
)
```

异步客户端使用完全相同的接口。如果您传递 [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) 实例，文件内容将自动异步读取。

## Webhook 验证

验证 webhook 签名是 _可选但建议的_。

有关 webhook 的更多信息，请参见 [API 文档](https://platform.openai.com/docs/guides/webhooks)。

### 解析 webhook 负载

对于大多数用例，您可能希望同时验证 webhook 并解析负载。为了实现这一点，我们提供了 `client.webhooks.unwrap()` 方法，该方法解析 webhook 请求并验证它是否由 OpenAI 发送。如果签名无效，此方法将引发错误。

请注意，`body` 参数必须是从服务器发送的原始 JSON 字符串（不要先解析它）。`.unwrap()` 方法将在验证 webhook 是由 OpenAI 发送后为您将此 JSON 解析为事件对象。

```python
from openai import OpenAI
from flask import Flask, request

app = Flask(__name__)
client = OpenAI()  # 默认使用 OPENAI_WEBHOOK_SECRET 环境变量


@app.route("/webhook", methods=["POST"])
def webhook():
    request_body = request.get_data(as_text=True)

    try:
        event = client.webhooks.unwrap(request_body, request.headers)

        if event.type == "response.completed":
            print("响应完成:", event.data)
        elif event.type == "response.failed":
            print("响应失败:", event.data)
        else:
            print("未处理的事件类型:", event.type)

        return "ok"
    except Exception as e:
        print("无效签名:", e)
        return "无效签名", 400


if __name__ == "__main__":
    app.run(port=8000)
```

### 直接验证 webhook 负载

在某些情况下，您可能希望将验证 webhook 与解析负载分开处理。如果您希望分别处理这些步骤，我们提供了 `client.webhooks.verify_signature()` 方法来 _仅验证_ webhook 请求的签名。与 `.unwrap()` 一样，如果签名无效，此方法将引发错误。

请注意，`body` 参数必须是从服务器发送的原始 JSON 字符串（不要先解析它）。验证签名后，您将需要解析主体。

```python
import json
from openai import OpenAI
from flask import Flask, request

app = Flask(__name__)
client = OpenAI()  # 默认使用 OPENAI_WEBHOOK_SECRET 环境变量


@app.route("/webhook", methods=["POST"])
def webhook():
    request_body = request.get_data(as_text=True)

    try:
        client.webhooks.verify_signature(request_body, request.headers)

        # 验证后解析主体
        event = json.loads(request_body)
        print("已验证事件:", event)

        return "ok"
    except Exception as e:
        print("无效签名:", e)
        return "无效签名", 400


if __name__ == "__main__":
    app.run(port=8000)
```

## 错误处理

当库无法连接到 API 时（例如，由于网络连接问题或超时），将引发 `openai.APIConnectionError` 的子类。

当 API 返回非成功状态码（即 4xx 或 5xx
响应）时，将引发 `openai.APIStatusError` 的子类，包含 `status_code` 和 `response` 属性。

所有错误都继承自 `openai.APIError`。

```python
import openai
from openai import OpenAI

client = OpenAI()

try:
    client.fine_tuning.jobs.create(
        model="gpt-4o",
        training_file="file-abc123",
    )
except openai.APIConnectionError as e:
    print("无法访问服务器")
    print(e.__cause__)  # 底层异常，可能由 httpx 引发。
except openai.RateLimitError as e:
    print("收到 429 状态码；我们应该稍微退避一下。")
except openai.APIStatusError as e:
    print("收到另一个非 200 范围的状态码")
    print(e.status_code)
    print(e.response)
```

错误代码如下：

| 状态码 | 错误类型                   |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

## 请求 ID

> 有关调试请求的更多信息，请参见[这些文档](https://platform.openai.com/docs/api-reference/debugging-requests)

SDK 中的所有对象响应都提供一个 `_request_id` 属性，该属性从 `x-request-id` 响应头添加，以便您可以快速记录失败的请求并将其报告给 OpenAI。

```python
response = await client.responses.create(
    model="gpt-4o-mini",
    input="说‘这是一个测试’。",
)
print(response._request_id)  # req_123
```

请注意，与其他使用 `_` 前缀的属性不同，`_request_id` 属性
_是_ 公开的。除非另有说明，_所有_ 其他 `_` 前缀属性、
方法和模块都是 _私有_ 的。

> [!重要]  
> 如果您需要访问失败请求的请求 ID，您必须捕获 `APIStatusError` 异常

```python
import openai

try:
    completion = await client.chat.completions.create(
        messages=[{"role": "user", "content": "说这是一个测试"}], model="gpt-4"
    )
except openai.APIStatusError as exc:
    print(exc.request_id)  # req_123
    raise exc
```

## 重试

某些错误默认会自动重试 2 次，使用较短的指数退避。
连接错误（例如，由于网络连接问题）、408 请求超时、409 冲突、
429 速率限制和 >=500 内部错误都默认会重试。

您可以使用 `max_retries` 选项来配置或禁用重试设置：

```python
from openai import OpenAI

# 为所有请求配置默认值：
client = OpenAI(
    # 默认值为 2
    max_retries=0,
)

# 或者，为每个请求配置：
client.with_options(max_retries=5).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "如何在 JavaScript 中获取当前日期的名称？",
        }
    ],
    model="gpt-4o",
)
```

## 超时

默认情况下，请求在 10 分钟后超时。您可以使用 `timeout` 选项进行配置，
该选项接受浮点数或 [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) 对象：

```python
from openai import OpenAI

# 为所有请求配置默认值：
client = OpenAI(
    # 20 秒（默认值为 10 分钟）
    timeout=20.0,
)

# 更精细的控制：
client = OpenAI(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# 为每个请求覆盖：
client.with_options(timeout=5.0).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "如何使用 Python 列出目录中的所有文件？",
        }
    ],
    model="gpt-4o",
)
```

超时时，会引发 `APITimeoutError`。

请注意，超时的请求[默认会重试两次](#重试)。

## 高级功能

### 日志记录

我们使用标准库 [`logging`](https://docs.python.org/3/library/logging.html) 模块。

您可以通过设置环境变量 `OPENAI_LOG` 为 `info` 来启用日志记录。

```shell
$ export OPENAI_LOG=info
```

或者设置为 `debug` 以获取更详细的日志记录。

### 如何区分 `None` 表示 `null` 还是缺失

在 API 响应中，字段可能是显式的 `null`，或者完全缺失；在这两种情况下，其值在此库中都是 `None`。您可以使用 `.model_fields_set` 来区分这两种情况：

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('收到类似 {} 的 json，完全没有 "my_field" 键。')
  else:
    print('收到类似 {"my_field": null} 的 json。')
```

### 访问原始响应数据（例如标头）

可以通过在任何 HTTP 方法调用前加上 `.with_raw_response.` 来访问 "原始" Response 对象，例如，

```py
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.with_raw_response.create(
    messages=[{
        "role": "user",
        "content": "说这是一个测试",
    }],
    model="gpt-4o",
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # 获取 `chat.completions.create()` 会返回的对象
print(completion)
```