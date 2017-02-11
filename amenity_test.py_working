#!/usr/bin/python3
import unittest
from models.amenity import Amenity
import datetime


class AmenityTest(unittest.TestCase):
    def  setUp(self):
        """
        objects for testing
        """
        self.model1_test = Amenity()
        self.model2_test = Amenity()

    def test_instantiation(self):
        """
        class attributes initialization testing
         """
        self.assertIsInstance(self.model1_test, Amenity)
        self.assertIsInstance(self.model2_test, Amenity)
        self.assertTrue(hasattr(self.model1_test, "name"))
        self.assertTrue(self.model1_test.id != self.model2_test.id)
        
    def test_reinstantiation(self):
        model1_ctime = self.model1_test.created_at
        model2_ctime = self.model2_test.created_at
        self.assertTrue(model1_ctime != model2_ctime)
        self.assertTrue(type(model1_ctime) is datetime.datetime)

    def test_types(self):
        """
        attributes
        """
        self.assertTrue(type(self.model1_test.name) is str)


    def test_save(self):
        """
        saving updates the updated_at attribute
        """
        model1_utime = self.model1_test.updated_at
        self.model1_test.save()
        model1_stime = self.model1_test.updated_at
        self.assertFalse(model1_utime == model1_stime)

if __name__ == '__main__':
    unittest.main()
