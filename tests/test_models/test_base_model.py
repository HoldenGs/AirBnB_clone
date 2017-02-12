#!/usr/bin/python3
import unittest
from  models import BaseModel
import datetime


class BaseModelTest(unittest.TestCase):
    def  setUp(self):
        """
        objects to be tested
        """
        self.model1_test = BaseModel()
        self.model2_test = BaseModel()

    def test_instantiation(self):
        """
        test model instantianion
        to_json method of BaseModel class
        """
        self.assertIsInstance(self.model1_test, BaseModel)
        self.assertIsInstance(self.model2_test, BaseModel)
        self.assertTrue(hasattr(self.model1_test, "id"))
        self.assertTrue(hasattr(self.model1_test, "__class__"))
        self.assertTrue(hasattr(self.model1_test, "created_at"))
        self.assertTrue(self.model1_test.id != self.model2_test.id)

    def test_reinstantiation(self):
        model1_ctime = self.model1_test.created_at
        model2_ctime = self.model2_test.created_at
        self.assertTrue(model1_ctime != model2_ctime)
        self.assertTrue(type(model1_ctime) is datetime.datetime)

        """can't figure out how to test whether "save" does update"""
        """Need better understanding of HoldenGs code"""
        """
        def test_save(self):
        self.model2_test.save()
        m1u_time = self.model2_test.updated_at
        self.model2_test.save()
        m1u_saved_time = self.model2_test.updated_at
        self.assertFalse(m1u_time == m1u_saved_time)
        """

        """ can't figure out how to test diffs between output & in memory objects"""
        """ Need better understanding of HoldenGs code"""
        """
        def test_to_json(self):
        """
        """
        dict_m1 = self.model1_test.to_json()
        dict_m1 = self.model2_test.to_json()
        self.assertTrue(hasattr(dict_m1, "__class__"))
        self.assertTrue(dict_m1 != self.model1_test.__dict__)
        self.assertEqual(dict_m1["id"], self.model1_test.__dict__["id"])
        self.assertNotEqual(dict_m1["created_at"],
                            self.model1_test.__dict__["created_at"])
        self.assertNotEqual(type(dict_m1["created_at"]),
                            type(self.model1_test.__dict__["created_at"]))
        self.assertNotEqual(dict_m1, dict_m2)
        """

if __name__ == '__main__':
    unittest.main()
