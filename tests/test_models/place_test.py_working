#!/usr/bin/python3
import unittest
from models.place import Place
import datetime


class PlaceTest(unittest.TestCase):
    def  setUp(self):
        """
        objects for testing
        """
        self.model1_test = Place()
        self.model2_test = Place()

    def test_instantiation(self):
        """
        class attributes initialization testing
         """
        self.assertIsInstance(self.model1_test, Place)
        self.assertIsInstance(self.model2_test, Place)
        self.assertTrue(hasattr(self.model1_test, "name"))
        self.assertTrue(hasattr(self.model1_test, "city_id"))
        self.assertTrue(hasattr(self.model2_test, "user_id"))
        self.assertTrue(hasattr(self.model1_test, "number_rooms"))
        self.assertTrue(hasattr(self.model1_test, "number_bathrooms"))
        self.assertTrue(hasattr(self.model2_test, "latitude"))
        self.assertTrue(hasattr(self.model1_test, "amenities"))
        self.assertTrue(hasattr(self.model1_test, "latitude"))
        self.assertTrue(self.model1_test.id != self.model2_test.id)

    def test_types(self):
        """
        isntance attribute
        """
        self.assertTrue(type(self.model1_test.amenities) is str)
        self.assertTrue(type(self.model1_test.name) is str)
        self.assertTrue(type(self.model1_test.city_id) is str)
        self.assertTrue(type(self.model1_test.user_id) is str)
        self.assertTrue(type(self.model1_test.description) is str)
        self.assertTrue(type(self.model1_test.number_rooms) is int)
        self.assertTrue(type(self.model1_test.number_bathrooms) is int)
        self.assertTrue(type(self.model1_test.max_guest) is int)
        self.assertTrue(type(self.model1_test.price_by_night) is int)
        self.assertTrue(type(self.model1_test.longitude) is float)
        self.assertTrue(type(self.model1_test.latitude) is float)

    def test_save(self):
        """
        updating the updated_at attribute
        """
        model1_utime = self.model1_test.updated_at
        self.model1_test.save()
        model1_stime = self.model1_test.updated_at
        self.assertFalse(model1_utime == model1_stime)

if __name__ == '__main__':
    unittest.main()
