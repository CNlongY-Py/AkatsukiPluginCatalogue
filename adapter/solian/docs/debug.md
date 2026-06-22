# `debug.py` — `/solian_api` 调试命令

通过 HTTP SDK 或 WS 客户端直接调用 Solian API。

## 命令

```
/solian_api <account> <method_path> [json_args]
```

### 示例

```
/solian_api Akatsuki accounts.get_current_account
/solian_api Akatsuki accounts.get_account_by_username {"username":"test"}
/solian_api Akatsuki ws.send {"type":"ping","data":{}}
/solian_api Akatsuki ws.status
/solian_api Akatsuki ws.latency
```

## 路由

- `ws.*` 前缀 → 对 `SolianWSClient` 实例调用 `path[3:]`
- 其他 → 对 `SolarNetworkClient` HTTP 实例按 `.` 分割逐级 attribute 访问

## 输出

- `dict` / `list` → 缩进 2 空格 JSON，每行前缀 `  `
- 其他 → `= 值`

## 补全

`_ApiCompleter` 两步补全：
1. 账户名（`session.list_accounts()`）
2. 常用方法路径（约 50+ 个，涵盖 accounts/chat/sphere/wallet/auth/notifications/thoughts/drive/ws）
