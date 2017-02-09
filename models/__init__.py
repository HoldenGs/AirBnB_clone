#!/usr/bin/python3


__all__ = ["BaseModel"]

from engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
