#!/usr/bin/python3
"""engine/file_storage.py.
"""
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """ FileStorage class."""

    def test_save(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_new(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_newNone(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_NNnew(self):
        B = BaseModel()
        U = User()
        S = State()
        P = Place()
        C = City()
        A = Amenity()
        R = Review()
        models.storage.new(B)
        models.storage.new(U)
        models.storage.new(S)
        models.storage.new(P)
        models.storage.new(C)
        models.storage.new(A)
        models.storage.new(R)
        self.assertIn("BaseModel." + B.id, models.storage.all().keys())
        self.assertIn(B, models.storage.all().values())
        self.assertIn("User." + U.id, models.storage.all().keys())
        self.assertIn(U, models.storage.all().values())
        self.assertIn("State." + S.id, models.storage.all().keys())
        self.assertIn(S, models.storage.all().values())
        self.assertIn("Place." + P.id, models.storage.all().keys())
        self.assertIn(P, models.storage.all().values())
        self.assertIn("City." + C.id, models.storage.all().keys())
        self.assertIn(C, models.storage.all().values())
        self.assertIn("Amenity." + A.id, models.storage.all().keys())
        self.assertIn(A, models.storage.all().values())
        self.assertIn("Review." + R.id, models.storage.all().keys())
        self.assertIn(R, models.storage.all().values())

    def test_rearg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_inst(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_objisdict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage(self):
        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
