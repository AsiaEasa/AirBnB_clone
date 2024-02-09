#!/usr/bin/python3
"""unittests for state
"""
import models
import unittest
from datetime import datetime
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """State"""

    def test_cls_type(self):
        self.assertEqual(State, type(State()))

    def test_storge_object(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_type(self):
        self.assertEqual(str, type(State.name))

    def test_args_unused(self):
        N = State(None)
        self.assertNotIn(None, N.__dict__.values())

    def test_intTypeError(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_no_args(self):
        M = State()
        self.assertIsInstance(M, State)

    def test_save_arg(self):
        N = State()
        with self.assertRaises(TypeError):
            N.save(None)

    def test_to_dict_1(self):
        N = State()
        self.assertNotEqual(N.to_dict(), N.__dict__)

    def test_to_dict_2(self):
        N = State()
        with self.assertRaises(TypeError):
            N.to_dict(None)

    def test_h(self):
        M = State()
        self.assertEqual(M.name, "")

    def test_name_attr(self):
        M = State()
        self.assertIn("name", dir(M))

    def test_k(self):
        M = State()
        self.assertNotIn("name", M.__dict__)

    def test_ids(self):
        N1 = State()
        N2 = State()
        self.assertNotEqual(N1.id, N2.id)

    def test_attributes_assignment(self):
        N = State()
        N.name = "Khartum"
        self.assertEqual(N.name, "Khartum")

    def test_2_created_at(self):
        N1 = State()
        N2 = State()
        self.assertLess(N1.created_at, N2.created_at)

    def test_2_updated_at(self):
        N1 = State()
        N2 = State()
        self.assertLess(N1.updated_at, N2.updated_at)

    def test_str_rep(self):
        """ sec"""
        D = datetime.today()
        D_repr = repr(D)
        N = State()
        N.id = "12344"
        N.created_at = N.updated_at = D
        ST = N.__str__()
        self.assertIn("[State] (12344)", ST)
        self.assertIn("'id': '12344'", ST)
        self.assertIn("'created_at': " + D_repr, ST)
        self.assertIn("'updated_at': " + D_repr, ST)

    def test_equal_of_ins(self):
        """ sec"""
        D = datetime.today()
        D_IOS = D.isoformat()
        N = State(id="3333", created_at=D_IOS, updated_at=D_IOS)
        self.assertEqual(N.id, "3333")
        self.assertEqual(N.created_at, D)
        self.assertEqual(N.updated_at, D)

    def test_save(self):
        """ sec"""
        N = State()
        F = N.updated_at
        N.save()
        L = N.updated_at
        self.assertLess(F, L)


if __name__ == "__main__":
    unittest.main()
