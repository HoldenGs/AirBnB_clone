#!/usr/bin/python3
import unittest
from models.user import User
from datetime import datetime


class UserTest(unittest.TestCase):
    def  setUp(self):
        """
        objects for testing
        """
        self.model1_test = User()


    def test_instantiation(self):
        """
        class attributes initialization testing
         """
        self.assertIsInstance(self.model1_test, User)
        self.assertTrue(hasattr(self.model1_test, "email"))
        self.assertTrue(hasattr(self.model1_test, "password"))
        self.assertTrue(hasattr(self.model1_test, "first_name"))
        self.assertTrue(hasattr(self.model1_test, "last_name"))


    def test_types(self):
        """
        instance attributes are str type
         """
        self.assertTrue(type(self.model1_test.email) is str)
        self.assertTrue(type(self.model1_test.password) is str)
        self.assertTrue(type(self.model1_test.first_name) is str)
        self.assertTrue(type(self.model1_test.last_name) is str)

                        
if __name__ == '__main__':
    unittest.main()
