#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
import json


class Test_file_storage(unittest.TestCase):
    """Test case for file storage """

    def setUp(self):
        """Seting up the required Test Cases"""
        self.file = FileStorage()
        self.all = self.file.all()

    def test_filePath(self):
        """Test if the file path exist and are same"""
        self.assertEqual(self.file._FileStorage__file_path,
                         FileStorage._FileStorage__file_path)

    def test_object(self):
        """Checks if __objects is a Dictionary"""
        self.assertIsInstance(self.file._FileStorage__objects, dict)

    def test_all(self):
        """Checks if the all function returns a Dictionary"""
        self.assertIsInstance(self.all, dict)

    # def test_save(self):
    #     test_data = {
    #         "user": {"age": 20},
    #         "value": {"hobbie": "coding"}
    #     }

    #     self.file.__objects = test_data

    #     self.file.save()

    #     with open("file.json", "r") as f:
    #         data = json.loads(f)

    #     self.assertEqual(data, test_data)


if __name__ == "__main__":
    unittest.main()
