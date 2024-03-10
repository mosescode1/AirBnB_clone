#!/usr/bin/python3

from models.user import User
from models import storage
import unittest


class Test_user(unittest.TestCase):
    def setUp(self):
        """ Setting up the model to run for all test """
        self.user = User()
        self.user.name = "My first model"
        self.user.my_number = 98
        self.user.save()

    def test_user_id(self):
        print(self.user.id)

        self.assertEqual(self.user.name, "My first model")

    def test_user_id(self):
        self.assertEqual(self.user.my_number, 98)

    def test_instance(self):
        self.assertIsInstance(self.user.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
