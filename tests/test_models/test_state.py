#!/usr/bin/python3
""" Import unittest and created a class for unit test """
import os
from datetime import datetime
import unittest
from models.state import State
import models.state


class TestStateDocumentation(unittest.TestCase):
    """ Create a tests for the User class in documentation
    and requirements """

    def test_style_pep8_model(self):
        """ PEP8 python style """
        style_model = os.system("pep8 models/state.py")
        self.assertEqual(style_model, 0)

    def test_style_pep8(self):
        """ PEP8 python style """
        style_test = os.system("pep8 tests/test_models/test_state.py")
        self.assertEqual(style_test, 0)

    def test_shebang(self):
        """ Test shebang in the front line """
        with open("models/state.py", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_shebang_test(self):
        """ Test shebang in the front line in test file """
        with open("tests/test_models/test_state.py", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_module_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.state.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(State.__doc__) != 0)


class TestState(unittest.TestCase):
    """ Create a tests for the class State in edge cases """
    def test_exists(self):
        """ This method checks for class of an object """
        object = State()
        self.assertEqual(object.__class__, State)

    def test_attribute(self):
        """ This method checks for a public class attribute """
        self.assertIsInstance(State.name, str)
