#!/usr/bin/python3
"""Defines unittests for console.py"""

import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_create(unittest.TestCase):
    """create"""

    def test_mis(self):
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
        items = ["all", "count", "destroy", "show", "update"]
        for item in items:
            with patch("sys.stdout", new=StringIO()) as FF:
                self.assertFalse(HBNBCommand().onecmd(f"{item} kkk"))
                self.assertEqual(X, FF.getvalue().strip())

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as FF:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", FF.getvalue().strip())

    def test_EOF_quit(self):
        items = ["EOF", "quit"]
        for item in items:
            with patch("sys.stdout", new=StringIO()) as FF:
                self.assertTrue(HBNBCommand().onecmd(f"{item}"))

    def test_help_quit(self):
        X = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as FF:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(X, FF.getvalue().strip())
