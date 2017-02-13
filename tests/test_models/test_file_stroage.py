#!/usr/bin/python3
"""This unittest tries testing file_storage, incomplete"""

import os
import tempfile
import time
import unittest
from models import *


class FileStorageTest(unittest.TestCase):
  def setUp(self):
    self._storage_path = tempfile.mkdtemp()      
    self._storage = FileStorage.Storage(self._storage_path)

  def tearDown(self):
    os.removedirs(self._storage_path)
