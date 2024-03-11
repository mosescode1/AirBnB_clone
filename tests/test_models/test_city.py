#!/usr/bin/python3

from models.city import City
# from models import storage
import unittest


class Test_city(unittest.TestCase):
    def setUp(self):
        """ Setting up the model to run for all test """
        self.city = City()
        self.city.name = "My first model"
        self.city.my_number = 98
        self.city.save()

    def test_user_id(self):
        print(self.city.id)

        self.assertEqual(self.city.name, "My first model")

    def test_user_id(self):
        self.assertEqual(self.city.my_number, 98)

    def test_instance(self):
        self.assertIsInstance(self.city.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
