from __future__ import annotations

from enum import IntEnum


class AbuseReportType(IntEnum):
    copyright = 0
    harassment = 1
    impersonation = 2
    offensive_content = 3
    spam = 4
    privacy_violation = 5
    illegal_content = 6
    other = 7
