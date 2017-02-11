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

    def basic_setup_test(self):
        """
        test model instantianion
        to_json method of BaseModel class
        """
        self.assertIsInstance(self.model1_test, BaseModel)
        self.assertIsInstance(self.model2_test, BaseModel)
        self.assertTrue(hasattr(self.model1_test, "id"))
        self.assertTrue(hasattr(self.model1_test, "__class__"))
        self.assertTrue(hasattr(self.model1_test, "created_at"))
        self.assertTrue(hasattr(self.model1_test, "updated_at"))
        self.assertTrue(self.model1_test.id != self.model2_test.id)
        model1_ctime = self.model1_test.created_at
        model2_ctime = self.model2_test.created_at
        self.assertTrue(model1_ctime != modle2_ctime)
        self.assertTrue(type(model1_ctime) is datetime.datetime)

    def test_save(self):
        """
        saving updates the updated_at attribute
        """
        model1_utime = self.model1_test.updated_at
        self.model1_test.save()
        modle1_stime = self.model1_test.updated_at
        self.assertFalse(model1_utime == model1_stime)

    def test_to_json(self):
        """
        to_json method testing
        """
        model2_testid = self.model2_test.id
        jsondict_obj = self.model2_test.to_json()
        self.assertNotEqual(self.model2_test.__dict__, jsondict_obj)
        self.assertNotIsInstance(jsondict_obj["created_at"], datetime)
        self.assertNotIsInstance(jsondict_obj["updated_at"], datetime)
        self.assertEqual(jsondict_obj["id"], self.model2_test.__dict__["id"])
        self.assertNotEqual(jsondict_obj["created_at"],
                            self.model2_test.__dict__["created_at"])
        self.assertNotEqual(type(jsondict_obj["created_at"]),
                            type(self.model2_test.__dict__["created_at"]))
        self.assertEqual(jsondict_obj["__class__"], "BaseModel")

if __name__ == '__main__':
    unittest.main()
