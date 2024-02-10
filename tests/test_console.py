#!/usr/bin/python3
"""Defines unittests for console.py"""

import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_create(unittest.TestCase):
    """create"""

    def test_smissing_cla(self):
        MSG = "** class name missing **"
        CO = ["show", ".show()", ]
        for C in CO:
            with patch("sys.stdout", new=StringIO()) as OUT:
                self.assertFalse(HBNBCommand().onecmd(C))
                self.assertEqual(MSG, OUT.getvalue().strip())

    def test_desmissing_cla(self):
        MSG = "** class name missing **"
        CO = ["destroy", ".destroy()"]
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

    def test_count_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
