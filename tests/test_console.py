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

    def test_mis_all(self):
        X = "** class doesn't exist **"
        items = ["count", "all"]
        for item in items:
            with patch("sys.stdout", new=StringIO()) as FF:
            self.assertFalse(HBNBCommand().onecmd(f"MyModel.{item}()"))
            self.assertEqual(X, FF.getvalue().strip())

    def test_update_miss(self):
        correct = "** value missing **"
