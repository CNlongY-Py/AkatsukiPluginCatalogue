import json
import logging
import threading
import time
import traceback

import websocket

from plugins.solian.define import HEARTBEAT_INTERVAL, RECONNECT_DELAY, RECONNECT_MAX_DELAY, WS_URL

_log = logging.getLogger("solian.ws")


class SolianWSClient:
    def __init__(self, log=None):
        self._ws = None
        self._token = None
        self._connected = False
        self._stop = False
        self._reconnect_delay = RECONNECT_DELAY
        self._latency = 0.0
        self._log = log or _log
        self._close_code = 1005
        self._close_reason = ""

        self.on_open = None
        self.on_message = None
        self.on_close = None

    @property
    def connected(self):
        return self._connected

    @property
    def latency(self):
        return self._latency

    def start(self, token):
        self._token = token
        self._stop = False
        _thread = threading.Thread(target=self._run, daemon=True)
        _thread.start()

    def stop(self):
        self._stop = True
        if self._ws:
            self._ws.close()
            self._ws = None
        self._connected = False

    def send(self, data):
        if not self._connected or not self._ws:
            self._log.warning("send skipped — not connected")
            return False
        try:
            self._ws.send(json.dumps(data))
            return True
        except Exception:
            self._log.error(f"send failed\n{traceback.format_exc()}")
            return False

    def status(self):
        return {
            "connected": self._connected,
            "latency": self._latency,
            "reconnect_delay": self._reconnect_delay,
        }

    def _log_close(self):
        reason = self._close_reason or ""
        self._log.info(f'websocket closed: status_code={self._close_code} reason="{reason}"')

    def _sleep_reconnect(self):
        self._log.info(f"reconnecting in {self._reconnect_delay:.1f}s ...")
        deadline = time.monotonic() + self._reconnect_delay
        while time.monotonic() < deadline and not self._stop:
            time.sleep(0.5)
        self._reconnect_delay = min(self._reconnect_delay * 2, RECONNECT_MAX_DELAY)

    def _run(self):
        while not self._stop:
            try:
                url = f"{WS_URL}?tk={self._token}"
                self._log.info(f"connecting to {WS_URL} ...")

                def _on_open(ws):
                    self._connected = True
                    self._reconnect_delay = RECONNECT_DELAY
                    self._log.info(f"connected to {WS_URL}")
                    if self.on_open:
                        self.on_open()

                def _on_message(ws, message):
                    try:
                        msg = json.loads(message)
                    except json.JSONDecodeError:
                        self._log.warning("invalid json received")
                        return
                    self._log.debug(f"<< {msg.get('type')}")
                    if self.on_message:
                        self.on_message(msg)

                def _on_close(ws, close_status_code, close_msg):
                    self._close_code = close_status_code or 1005
                    self._close_reason = close_msg or ""
                    self._connected = False
                    if self.on_close:
                        self.on_close(self._close_code, self._close_reason)
                    self._log_close()

                def _on_error(ws, error):
                    self._log.warning(f"ws error: {error}")

                def _on_pong(ws, message):
                    if ws.last_ping_tm:
                        self._latency = (time.monotonic() - ws.last_ping_tm) * 1000
                        self._log.debug(f"heartbeat {self._latency:.0f}ms")

                ws = websocket.WebSocketApp(
                    url,
                    on_open=_on_open,
                    on_message=_on_message,
                    on_close=_on_close,
                    on_error=_on_error,
                    on_pong=_on_pong,
                )
                self._ws = ws
                ws.run_forever(ping_interval=HEARTBEAT_INTERVAL, ping_timeout=10)
                self._ws = None
                if self._stop:
                    return
                self._log.info("reconnecting ...")
                self._sleep_reconnect()
            except Exception:
                self._log.error(f"connect failed\n{traceback.format_exc()}")
                if self._stop:
                    return
                self._sleep_reconnect()
