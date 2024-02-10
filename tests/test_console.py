#!/usr/bin/python3
"""Defines unittests for console.py"""

import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_create(unittest.TestCase):
    """create"""

    def test_mis_class(self):
        X = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as FF:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(X, FF.getvalue().strip())

    def test_mis_1(self):
        X = "** class doesn't exist **"
        items = ["all", "count"]
        for item in items:
            with patch("sys.stdout", new=StringIO()) as FF:
                self.assertFalse(HBNBCommand().onecmd(f"kkk.{item}()"))
                self.assertEqual(X, FF.getvalue().strip())

    def test_mis_2(self):
        X = "** class doesn't exist **"
        items = ["all", "count", "destroy", "show", "update", "create"]
        for item in items:
            with patch("sys.stdout", new=StringIO()) as FF:
                self.assertFalse(HBNBCommand().onecmd(f"{item} kkk"))
                self.assertEqual(X, FF.getvalue().strip())

    def test_invalid_1(self):
        items = ["destroy", "show", "update", "create"]
        for item in items:
            X = f"*** Unknown syntax: kkk.{item}()"
            with patch("sys.stdout", new=StringIO()) as FF:
                self.assertFalse(HBNBCommand().onecmd(f"kkk.{item}()"))
                self.assertEqual(X, FF.getvalue().strip())

    def misName(self):
 
        X = "** class name missing **"
        ops["destroy", "show", "create",".destroy", ".show"]
        for op in ops:
            with patch("sys.stdout", new=StringIO()) as OO:
                self.assertFalse(HBNBCommand().onecmd(op))
                self.assertEqual(X, OO.getvalue().strip())

