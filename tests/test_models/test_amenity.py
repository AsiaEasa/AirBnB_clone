#!/usr/bin/python3
"""unittests for models/amenity.py.
"""

import os
import models
import unittest
from datetime import datetime
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """Amenity"""

    def test_cls_type(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_storge_object(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_type(self):
        self.assertEqual(str, type(Amenity.name))

    def test_args_unused(self):
        N = Amenity(None)
        self.assertNotIn(None, N.__dict__.values())

    def test_intTypeError(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_no_args(self):
        M = Amenity()
        self.assertIsInstance(M, Amenity)

    def test_save_arg(self):
        N = Amenity()
        with self.assertRaises(TypeError):
            N.save(None)

    def test_to_dict_1(self):
        N = Amenity()
        self.assertNotEqual(N.to_dict(), N.__dict__)

    def test_to_dict_2(self):
        N = Amenity()
        with self.assertRaises(TypeError):
            N.to_dict(None)

    def test_h(self):
        M = Amenity()
        self.assertEqual(M.name, "")

    def test_name_attr(self):
        M = Amenity()
        self.assertIn("name", dir(M))

    def test_k(self):
        M = Amenity()
        self.assertNotIn("name", M.__dict__)

    def test_ids(self):
        N1 = Amenity()
        N2 = Amenity()
        self.assertNotEqual(N1.id, N2.id)

    def test_attributes_assignment(self):
        N = Amenity()
        N.name = "Khartum"
        self.assertEqual(N.name, "Khartum")

    def test_2_created_at(self):
        N1 = Amenity()
        N2 = Amenity()
        self.assertLess(N1.created_at, N2.created_at)

    def test_2_updated_at(self):
        N1 = Amenity()
        N2 = Amenity()
        self.assertLess(N1.updated_at, N2.updated_at)

    def test_str_rep(self):
        """ sec"""
        D = datetime.today()
        D_repr = repr(D)
        N = Amenity()
        N.id = "12344"
        N.created_at = N.updated_at = D
        ST = N.__str__()
        self.assertIn("[Amenity] (12344)", ST)
        self.assertIn("'id': '12344'", ST)
        self.assertIn("'created_at': " + D_repr, ST)
        self.assertIn("'updated_at': " + D_repr, ST)

    def test_equal_of_ins(self):
        """ sec"""
        D = datetime.today()
        D_IOS = D.isoformat()
        N = Amenity(id="3333", created_at=D_IOS, updated_at=D_IOS)
        self.assertEqual(N.id, "3333")
        self.assertEqual(N.created_at, D)
        self.assertEqual(N.updated_at, D)

    def test_save(self):
        """ sec"""
        N = Amenity()
        F = N.updated_at
        N.save()
        L = N.updated_at
        self.assertLess(F, L)
