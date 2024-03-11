#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage


class Test_file_storage(unittest.TestCase):
    """Test case for file storage """

    def setUp(self):
        """Seting up the required Test Cases"""
        self.file = FileStorage()
        print(self.file.all())
