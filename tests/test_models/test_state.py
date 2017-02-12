#!/usr/bin/python3
import unittest
from models.state import State
from datetime import datetime


class StateTest(unittest.TestCase):
    def  setUp(self):
        """
        objects for testing
        """
        self.model1_test = State()
        self.model2_test = State()

    def test_instantiation(self):
        """
        class attributes initialization testing
         """
        self.assertIsInstance(self.model1_test, State)
        self.assertIsInstance(self.model2_test, State)
        self.assertTrue(hasattr(self.model1_test, "name"))

    def test_types(self):
        """
        instance attributes are str type
         """
        self.assertTrue(type(self.model1_test.name) is str)


                        
if __name__ == '__main__':
    unittest.main()
