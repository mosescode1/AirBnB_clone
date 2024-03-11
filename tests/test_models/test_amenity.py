#!/usr/bin/python3

from models.amenity import Amenity
# from models import storage
import unittest


class Test_amenity(unittest.TestCase):
    def setUp(self):
        """ Setting up the model to run for all test """
        self.amenity = Amenity()
        self.amenity.name = "My first model"
        self.amenity.my_number = 98
        self.amenity.save()

    def test_user_id(self):
        print(self.amenity.id)

        self.assertEqual(self.amenity.name, "My first model")

    def test_user_id(self):
        self.assertEqual(self.amenity.my_number, 98)

    def test_instance(self):
        self.assertIsInstance(self.amenity.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
