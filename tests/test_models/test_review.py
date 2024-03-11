#!/usr/bin/python3

from models.review import Review
# from models import storage
import unittest


class Test_review(unittest.TestCase):
    def setUp(self):
        """ Setting up the model to run for all test """
        self.review = Review()
        self.review.name = "My first model"
        self.review.my_number = 98
        self.review.save()

    def test_user_id(self):
        print(self.review.id)

        self.assertEqual(self.review.name, "My first model")

    def test_user_id(self):
        self.assertEqual(self.review.my_number, 98)

    def test_instance(self):
        self.assertIsInstance(self.review.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
