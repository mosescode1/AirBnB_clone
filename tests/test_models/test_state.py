#!/usr/bin/python3

from models.state import State
# from models import storage
import unittest


class Test_state(unittest.TestCase):
    def setUp(self):
        """ Setting up the model to run for all test """
        self.state = State()
        self.state.name = "My first model"
        self.state.my_number = 98
        self.state.save()

    def test_state_id(self):
        print(self.state.id)

        self.assertEqual(self.state.name, "My first model")

    def test_state_id(self):
        self.assertEqual(self.state.my_number, 98)

    def test_instance(self):
        self.assertIsInstance(self.state.__dict__, dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
