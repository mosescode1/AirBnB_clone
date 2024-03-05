#!/usr/bin/python3
""" A Basemodel testcases """
import unittest
from models.base_model import BaseModel
import datetime


class Test_BaseModel(unittest.TestCase):
    """ TESTING THE BASEMODEL FOR AIRBNB CLONE """

    def setUp(self):
        """ Setting up the model to run for all test """
        base = BaseModel()
        base.name = "My first model"
        base.my_number = 98
        base.created_at = datetime.dateime.now()

    def test_base_model_name(self):
        """Testing the base model name """
        self.assertEqual(self.base.name, "My first model")

    def test_base_model_number(self):
        """ testing the base mod number """
        self.assertEqual(self.base.my_number, 98)

    def test_base_model_id(self):
        """ Testing the base model id """
        self.assertTrue(self.base.id)

    def test_date_time(self):
        """ Testing the datetime """
        self.assertEqual(self.created_at, datetime.datetime.now())

    def test_base_model_created(self):
        """ Testing the time created """
        self.assertTrue(self.base.created_at)


if __name__ == "__main__":
    unittest.main()
