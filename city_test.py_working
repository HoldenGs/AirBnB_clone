#!/usr/bin/python3
import unittest
from models.city import City
import datetime


class CityTest(unittest.TestCase):
    def  setUp(self):
        """
        objects for testing
        """
        self.model1_test = City()
        self.model2_test = City()

    def test_instantiation(self):
        """
        initialization of class attributes
        """
        self.assertIsInstance(self.model1_test, City)
        self.assertIsInstance(self.model2_test, City)
        self.assertTrue(hasattr(self.model1_test, "state_id"))
        self.assertTrue(hasattr(self.model1_test, "name"))
        self.assertTrue(self.model1_test.id != self.model2_test.id)

    def test_types(self):
        """
        city attributes
        """
        self.assertTrue(type(self.model1_test.state_id) is str)
        self.assertTrue(type(self.model1_test.name) is str)

    def test_save(self):
        """
        updating updated_at attribute
        """
        model1_utime = self.model1_test.updated_at
        self.model1_test.save()
        model1_stime = self.model1_test.updated_at
        self.assertFalse(model1_utime == model1_stime)


if __name__ == '__main__':
    unittest.main()
