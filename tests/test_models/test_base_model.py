#!/usr/bin/python3
""" Import unittest and created a class for unit test """
import os
from datetime import datetime
import unittest
from models.base_model import BaseModel
import models.base_model


class TestBaseDocumentation(unittest.TestCase):
    """ Create a tests for the base class in documentation
    and requirements """
    def test_readme(self):
        """ Created a readme and that exists """
        theReadme = os.getcwd()
        readmeOne = theReadme + '/README.md'
        readmeTwo = os.path.exists(readmeOne)
        self.assertTrue(readmeTwo, True)
        with open(readmeOne, mode='r') as _file:
            readShebang = _file.read()
            self.assertTrue(len(readShebang) != 0)

    def test_style_pep8_model(self):
        """ PEP8 python style """
        style_model = os.system("pep8 models/base_model.py")
        self.assertEqual(style_model, 0)

    def test_style_pep8(self):
        """ PEP8 python style """
        style_test = os.system("pep8 tests/test_models/test_base_model.py")
        self.assertEqual(style_test, 0)

    def test_shebang(self):
        """ Test shebang in the front line """
        with open("models/base_model.py", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_shebang_test(self):
        """ Test shebang in the front line in test file """
        with open("tests/test_models/test_base_model.py", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_module_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.base_model.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(BaseModel.__doc__) != 0)

    def test_methods_doc(self):
        """ Methods with sufficient documentation """
        self.assertTrue(len(BaseModel.save.__doc__) != 0)
        self.assertTrue(len(BaseModel.to_dict.__doc__) != 0)


class TestBaseModel(unittest.TestCase):
    """ Create a tests for the base class BaseModel in edge cases """
    def test_attribute_id(self):
        """ Check to the id number that is a public instance attributes """
        object = BaseModel()
        object.dynamic = 'attr'
        inst = BaseModel()
        self.assertTrue(object.id != 0)
        self.assertTrue(type(object.id) is str)
        self.assertEqual(object.dynamic, 'attr')
        self.assertNotEqual(object.id, inst.id)

    def test_attribute_create_at(self):
        """ Check to the current datatime that is a public instance
            attributes """
        object = BaseModel()
        inst = BaseModel()
        self.assertTrue(object.created_at != 0)
        self.assertIsInstance(object.created_at, datetime)
        self.assertNotEqual(object.created_at, inst.created_at)
        self.assertNotEqual(object.updated_at, inst.updated_at)
        self.assertNotEqual(object.created_at, inst.updated_at)
        self.assertNotEqual(inst.created_at, object.updated_at)

    def test_attribute_updated_at(self):
        """ Check to the current datatime and will be updated that is a public
            instance attributes """
        object = BaseModel()
        self.assertTrue(object.updated_at != 0)
        self.assertIsInstance(object.updated_at, datetime)

    def test_save_method(self):
        """ Check instance of update_at that is datetime """
        # object = BaseModel()
        # object.save()
        # self.assertIsInstance(object.updated_at, datetime)
        self.object = BaseModel()
        date_old = self.object.updated_at
        self.object.save()
        self.assertNotEqual(date_old, self.object.updated_at)
        date_old = self.object.updated_at
        self.object.save()
        self.assertNotEqual(date_old, self.object.updated_at)

    def test_save(self):
        """Doc
        """
        pass

    def test_to_dict(self):
        """ Check returns the dictionary representation """
        object = BaseModel()
        object.my_number = 89
        object.name = "Holberton"
        obj = object.to_dict()
        self.assertIsInstance(obj, dict)
        self.assertTrue(len(obj) != 0)
        self.assertEqual(obj['updated_at'], object.to_dict()['updated_at'])

    def test_kwargs(self):
        """ Check that the instances created are not the same """
        object = BaseModel()
        object.my_number = 35
        object.name = "Betty"
        obj = object.to_dict()
        new_obj = BaseModel(**obj)
        self.assertFalse(object is new_obj)
        self.assertIsInstance(new_obj.created_at, datetime)
        self.assertIsInstance(new_obj.updated_at, datetime)
