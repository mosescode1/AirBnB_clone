#!/usr/bin/python3

from models.place import Place
# from models import storage
import unittest


class Test_place(unittest.TestCase):
    def setUp(self):
        """ Setting up the model to run for all test """
        self.place = Place()
        self.place.name = "My first model"
        self.place.my_number = 98
        self.place.save()

    def test_user_id(self):
        print(self.place.id)

        self.assertEqual(self.place.name, "My first model")

    def test_user_id(self):
        self.assertEqual(self.place.my_number, 98)

    def test_instance(self):
        self.assertIsInstance(self.place.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
