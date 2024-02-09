#!/usr/bin/python3
"""unittests for models/City.py.
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """City"""

    def test_cls_type(self):
        self.assertEqual(City, type(City()))

    def test_storge_object(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(City().updated_at))


    def test_args_unused(self):
        N = City(None)
        self.assertNotIn(None, N.__dict__.values())

    def test_intTypeError(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_no_args(self):
        M = City()
        self.assertIsInstance(M, City)

    def test_save_arg(self):
        N = City()
        with self.assertRaises(TypeError):
            N.save(None)

    def test_to_dict_1(self):
        N = City()
        self.assertNotEqual(N.to_dict(), N.__dict__)

    def test_to_dict_2(self):
        N = City()
        with self.assertRaises(TypeError):
            N.to_dict(None)

    def test_ids(self):
        N1 = City()
        N2 = City()
        self.assertNotEqual(N1.id, N2.id)

    def test_2_created_at(self):
        N1 = City()
        N2 = City()
        self.assertLess(N1.created_at, N2.created_at)

    def test_2_updated_at(self):
        N1 = City()
        N2 = City()
        self.assertLess(N1.updated_at, N2.updated_at)

    def test_name_type(self):
        self.assertEqual(str, type(City.name))


    def test_state_id_type(self):
        self.assertEqual(str, type(City.state_id))


    def test_state_id_attr(self):
        N = City()
        self.assertIn("state_id", dir(N))
        self.assertNotIn("state_id", N.__dict__)

    def test_name_attr(self):
        N = City()
        self.assertIn("name", dir(N))
        self.assertNotIn("name", N.__dict__)


    def test_str_rep(self):
        """ sec"""
        D = datetime.today()
        D_repr = repr(D)
        N = City()
        N.id = "12344"
        N.created_at = N.updated_at = D
        ST = N.__str__()
        self.assertIn("[City] (12344)", ST)
        self.assertIn("'id': '12344'", ST)
        self.assertIn("'created_at': " + D_repr, ST)
        self.assertIn("'updated_at': " + D_repr, ST)

    def test_equal_of_ins(self):
        """ sec"""
        D = datetime.today()
        D_IOS = D.isoformat()
        N = City(id="3333", created_at=D_IOS, updated_at=D_IOS)
        self.assertEqual(N.id, "3333")
        self.assertEqual(N.created_at, D)
        self.assertEqual(N.updated_at, D)

    def test_save(self):
        """ sec"""
        N = City()
        F = N.updated_at
        N.save()
        L = N.updated_at
        self.assertLess(F, L)



