# Solian 适配器

Solian 社交平台的多账户 WebSocket 客户端适配器，基于 `websocket-client`（同步）。

## 功能

- 多账户同时连接
- Token 文件导入，自动持久化
- 自动重连（指数退避，最大 60s）
- Heartbeat 延迟检测
- 命令补全 + AutoSuggest
- 账户绑定过滤（事件只投递到指定账户）
- HTTP/WS API 调试命令
- 内置消息打印（`Solian.Message`，可绑定账户）

## 环境要求

- Python 3.10+
- `websocket-client` 库

## 安装

```
pip install websocket-client
```

## 目录结构

```
solian/
├── __init__.py    # 主入口：命令注册 + 生命周期 + 绑定管理
├── api.py         # WebSocketApp 封装, 自动重连
├── debug.py       # /solian_api 调试命令
├── define.py      # 常量定义（URL, 事件名, 分组）
├── meta.json      # 插件元数据
├── msg.py         # 消息打印
├── sdk/           # SolarNetwork HTTP SDK
└── docs/          # 文档
```

## 快速开始

1. 获取 Solian API Token
2. 保存到纯文本文件 `<name>.token`
3. 在客户端中：

```
/solian import <name>.token
```

插件会自动连接并显示状态。

## 配置目录

```
./config/solian/
├── sessions/       # Token 文件（<name>.token）
└── sessions.json   # 账户元数据 + bindings
```

路径由 `payload.cfg` 控制，框架自动创建。

## 命令

| 命令 | 作用 |
|------|------|
| `/solian import <file>` | 导入 Token 文件，自动连接 |
| `/solian logout <name>` | 登出并删除账户 |
| `/solian reconnect [name]` | 重连（不指定 = 全部） |
| `/solian bind <plugin> <account>` | 绑定插件到账户 |
| `/solian unbind <plugin> [account]` | 解绑 |
| `/solian status` | 查看连接状态 + 绑定 |
| `/solian_api <account> <method> [json]` | 调用 HTTP/WS API |

## 事件

所有事件以 `solian.` 前缀触发。订阅示例：

```python
@events.on_event("solian.messages.new")
def handler(payload):
    print(f"[{payload.account}] {payload.data}")
```

完整事件列表见 `define.py`。
