# DefaultAioHttpClient 介绍

该文档介绍 OpenAI Python SDK 中的 `DefaultAioHttpClient`，它是一个使用 `aiohttp` 作为 HTTP 后端的异步客户端实现，适用于与 `AsyncOpenAI` 搭配以提高并发性能。

## 概览
- `DefaultAioHttpClient` 本质上是一个 `httpx.AsyncClient` 的变体，通过 `httpx_aiohttp` 将底层传输替换为 `aiohttp`。
- 与默认的 `httpx` 异步客户端相比，`aiohttp` 在高并发和长连接场景下通常有更好的表现。
- SDK 为其设置了合理的默认值：
  - `timeout = httpx.Timeout(timeout=600, connect=5.0)`（总超时 10 分钟，连接阶段 5 秒）
  - `limits = httpx.Limits(max_connections=1000, max_keepalive_connections=100)`（最大连接数 1000，保活连接数 100）
  - `follow_redirects = True`（默认跟随重定向）

## 安装与启用
1. 安装 aiohttp 扩展（推荐使用 SDK 提供的可选依赖）：
   ```sh
   pip install "openai[aiohttp]"
   ```
   这将安装 `aiohttp` 以及 `httpx_aiohttp`。

2. 在创建 `AsyncOpenAI` 客户端时传入 `http_client=DefaultAioHttpClient()`：
   ```python
   import asyncio
   from openai import AsyncOpenAI, DefaultAioHttpClient

   async def main() -> None:
       async with AsyncOpenAI(
           api_key="YOUR_API_KEY",
           http_client=DefaultAioHttpClient(),
       ) as client:
           resp = await client.responses.create(
               model="gpt-4o",
               input="这是一个 aiohttp 后端的测试",
           )
           print(resp.output_text)

   asyncio.run(main())
   ```

> 如果未安装上述可选依赖，实例化 `DefaultAioHttpClient` 会抛出：
> `RuntimeError: To use the aiohttp client you must have installed the package with the 'aiohttp' extra`

## 进阶配置
你可以像使用 `httpx.AsyncClient` 一样传参进行定制：
```python
from openai import AsyncOpenAI, DefaultAioHttpClient
import httpx

client = AsyncOpenAI(
    api_key="YOUR_API_KEY",
    http_client=DefaultAioHttpClient(
        timeout=httpx.Timeout(timeout=300, connect=3.0),  # 缩短总/连接超时
        limits=httpx.Limits(max_connections=2000, max_keepalive_connections=200),  # 提升并发上限
        follow_redirects=False,  # 禁用自动重定向
        proxies={"https": "http://proxy.example.com:8080"},  # 通过代理访问
        headers={"X-Custom": "foo"},  # 追加默认请求头
        verify=True,  # 校验证书（或提供 CA 路径）
    ),
)
```

常见可调参数（与 `httpx.AsyncClient` 对齐）：
- `timeout`：使用 `httpx.Timeout`，可分别设置 `connect`, `read`, `write`, `pool` 等超时；
- `limits`：使用 `httpx.Limits` 控制连接池上限、保活等；
- `proxies`：设置 HTTP(S) 代理；
- `headers`：为所有请求添加默认头；
- `verify`：TLS 校验相关设置；
- 其他 `httpx` 支持的客户端级参数基本兼容。

## 适用场景
- 高并发请求：如批量生成、向量检索、工具调用风格的并行任务。
- 长连接/流式传输：实时/流式响应（如 SSE 或 WebSocket 辅助的场景）。
- 事件循环统一：已有项目使用 `aiohttp`，希望保持后端一致性。

## 与 DefaultAsyncHttpxClient 的对比
- 相同点：二者均为 `httpx.AsyncClient` 形态的客户端，参数与行为几乎一致。
- 不同点：`DefaultAioHttpClient` 的传输为 `aiohttp`，在某些平台和负载下可能有更优的并发表现；同时需要额外依赖（`aiohttp` 与 `httpx_aiohttp`）。

## 资源关闭与生命周期
- SDK 已对连接的关闭进行了封装，推荐使用 `async with AsyncOpenAI(...)` 的上下文管理方式，退出时自动关闭。
- 若以非上下文方式使用，记得在适当时机调用 `await client.close()` 以释放连接。

## 常见问题排查
- 报错 `RuntimeError` 提示需要 `aiohttp extra`：确认已执行 `pip install "openai[aiohttp]"`，或已安装 `aiohttp` 和 `httpx_aiohttp`。
- 连接数不足/队列堆积：提升 `limits.max_connections`，或减少长时间占用连接的操作。
- 超时频繁：增大 `timeout` 或拆分任务批次；网络条件差时可考虑代理与重试策略。

## 参考
- 代码位置：`src/openai/_base_client.py`（`DefaultAioHttpClient` 定义与默认参数设定）
- 可选依赖：`pyproject.toml` 中的 `[project.optional-dependencies].aiohttp`
- 官方文档示例：`README.md` 与 `README_cn.md` 的 “使用 aiohttp” 部分