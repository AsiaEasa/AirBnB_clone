#!/usr/bin/python3
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TestHBNB(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_smissing_cla(self):
        MSG = "** class name missing **"
        CO = ["show"]
        for C in CO:
            with patch("sys.stdout", new=StringIO()) as OUT:
                self.assertFalse(HBNBCommand().onecmd(C))
                self.assertEqual(MSG, OUT.getvalue().strip())

    def test_crmissing_cla(self):
        MSG = "** class name missing **"
        CO = ["create"]
        for C in CO:
            with patch("sys.stdout", new=StringIO()) as OUT:
                self.assertFalse(HBNBCommand().onecmd(C))
                self.assertEqual(MSG, OUT.getvalue().strip())
    def test_desmissing_cla(self):
        MSG = "** class name missing **"
        CO = ["destroy"]
        for C in CO:
            with patch("sys.stdout", new=StringIO()) as OUT:
                self.assertFalse(HBNBCommand().onecmd(C))
                self.assertEqual(MSG, OUT.getvalue().strip())
    def test_mis_1(self):
        X = "** class doesn't exist **"
        items = ["all", "count"]
        for item in items:
            with patch("sys.stdout", new=StringIO()) as FF:
                self.assertFalse(HBNBCommand().onecmd(f"kkk.{item}()"))
                self.assertEqual(X, FF.getvalue().strip())

    def test_mis_2(self):
        X = "** class doesn't exist **"
        items = ["all", "count", "destroy", "show", "update"]
        for item in items:
            with patch("sys.stdout", new=StringIO()) as FF:
                self.assertFalse(HBNBCommand().onecmd(f"{item} kkk"))
                self.assertEqual(X, FF.getvalue().strip())  

    def test_invalid_1(self):
        items = ["create"]
        for item in items:
            X = f"*** Unknown syntax: kkk.{item}()"
            with patch("sys.stdout", new=StringIO()) as FF:
                self.assertFalse(HBNBCommand().onecmd(f"kkk.{item}()"))
                self.assertEqual(X, FF.getvalue().strip())

    def test_mis_all(self):
        X = "** class doesn't exist **"
        items = ["count", "all"]
        for item in items:
            with patch("sys.stdout", new=StringIO()) as FF:
                self.assertFalse(HBNBCommand().onecmd(f"MyModel.{item}()"))
                self.assertEqual(X, FF.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
