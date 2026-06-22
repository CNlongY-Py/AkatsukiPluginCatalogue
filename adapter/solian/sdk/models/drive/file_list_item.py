from __future__ import annotations

from enum import IntEnum
from typing import Union

from pydantic import BaseModel

from .file import SnCloudFile


class FileListItemType(IntEnum):
    file = 0
    folder = 1
    unindexed_file = 2


class FileListItem(BaseModel):
    type: FileListItemType = FileListItemType.file
    file: SnCloudFile | None = None
