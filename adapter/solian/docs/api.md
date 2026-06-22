# `api.py` — WebSocket 客户端

基于 `websocket-client` 的 `WebSocketApp`，提供自动重连和延迟检测。

## 类 `SolianWSClient`

### 构造函数

```python
SolianWSClient(log=None)
```

- `log` — 可选 Logger，默认使用 `logging.getLogger("solian.ws")`

### 属性

| 属性 | 类型 | 说明 |
|------|------|------|
| `connected` | bool | 是否已连接 |
| `latency` | float | 最近一次心跳延迟（ms） |

### 回调

| 属性 | 签名 | 触发时机 |
|------|------|----------|
| `on_open` | `()` | 连接建立 |
| `on_message` | `(dict)` | 收到 JSON 消息（已 parse） |
| `on_close` | `(code, reason)` | 连接关闭 |

### 方法

| 方法 | 说明 |
|------|------|
| `start(token)` | 启动新线程运行 `run_forever` |
| `stop()` | 关闭连接，重置状态 |
| `send(data)` | 发送 JSON dict，返回 bool |
| `status()` | 返回 `{connected, latency, reconnect_delay}` |

## 重连机制

- 初始延迟：`RECONNECT_DELAY`（5s）
- 指数退避，最大 `RECONNECT_MAX_DELAY`（60s）
- 每次成功连接后重置为初始值
- `_stop` 标志可在任意阶段中断重连

## 线程安全

- `start()` 创建 `daemon=True` 线程
- `stop()` 设置标志后调用 `ws.close()`，`run_forever` 返回后线程结束
- `on_open` / `on_message` / `on_close` 在 WS 线程中被调用
