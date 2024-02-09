#!/usr/bin/python3
"""unittests for base_model
"""
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """BaseModel"""

    def test_cls_type(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_storge_object(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_new_instance(self):
        N = BaseModel()
        self.assertIsInstance(N, BaseModel)
        self.assertTrue(hasattr(N, 'id'))
        self.assertTrue(hasattr(N, 'created_at'))
        self.assertTrue(hasattr(N, 'updated_at'))

    def test_id_type(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_args_unused(self):
        N = BaseModel(None)
        self.assertNotIn(None, N.__dict__.values())

    def test_str(self):
        N = BaseModel()
        STR = f"[BaseModel] ({N.id}) {N.__dict__}"
        self.assertEqual(str(N), STR)

    def test_str_2(self):
        N = BaseModel()
        STR = str(N)
        self.assertIsInstance(STR, str)
        self.assertIn('BaseModel', STR)
        self.assertIn(N.id, STR)

    def test_intTypeError(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_no_args(self):
        M = BaseModel()
        self.assertIsInstance(M, BaseModel)

    def test_save_arg(self):
        N = BaseModel()
        with self.assertRaises(TypeError):
            N.save(None)

    def test_to_dict_1(self):
        N = BaseModel()
        self.assertNotEqual(N.to_dict(), N.__dict__)

    def test_to_dict_2(self):
        N = BaseModel()
        with self.assertRaises(TypeError):
            N.to_dict(None)

    def test_to_dict_type(self):
        N = BaseModel()
        self.assertTrue(dict, type(N.to_dict()))

    def test_added_attr(self):
        N = BaseModel()
        N.Course = "python"
        N.content = 5
        N.com = "coursera"
        self.assertIn("Course", N.to_dict())
        self.assertIn("content", N.to_dict())
        self.assertIn("com", N.to_dict())

    def test_ids(self):
        N1 = BaseModel()
        N2 = BaseModel()
        self.assertNotEqual(N1.id, N2.id)

    def test_2_created_at(self):
        N1 = BaseModel()
        N2 = BaseModel()
        self.assertLess(N1.created_at, N2.created_at)

    def test_2_updated_at(self):
        N1 = BaseModel()
        N2 = BaseModel()
        self.assertLess(N1.updated_at, N2.updated_at)

    def test_str_rep(self):
        """ sec"""
        D = datetime.today()
        D_repr = repr(D)
        N = BaseModel()
        N.id = "12344"
        N.created_at = N.updated_at = D
        ST = N.__str__()
        self.assertIn("[BaseModel] (12344)", ST)
        self.assertIn("'id': '12344'", ST)
        self.assertIn("'created_at': " + D_repr, ST)
        self.assertIn("'updated_at': " + D_repr, ST)

    def test_equal_of_ins(self):
        """ sec"""
        D = datetime.today()
        D_IOS = D.isoformat()
        N = BaseModel(id="3333", created_at=D_IOS, updated_at=D_IOS)
        self.assertEqual(N.id, "3333")
        self.assertEqual(N.created_at, D)
        self.assertEqual(N.updated_at, D)

    def test_save_to_file(self):
        N = BaseModel()
        N.save()
        IN = f"BaseModel.{N.id}"
        with open("file.json", "r") as f_1:
            self.assertIn(IN, f_1.read())

    def test_equal_2(self):
        D = datetime.today()
        D_IOS = D.isoformat()
        N = BaseModel("10", id="3333", created_at=D_IOS, updated_at=D_IOS)
        self.assertEqual(N.id, "3333")
        self.assertEqual(N.created_at, D)
        self.assertEqual(N.updated_at, D)

    def test_to_dict(self):
        N = BaseModel()
        N1 = N.to_dict()
        self.assertIsInstance(N1, dict)
        self.assertIn('__class__', N1)
        self.assertIn('created_at', N1)
        self.assertIn('updated_at', N1)
        self.assertIn('id', N1)
        self.assertEqual(N1['__class__'], 'BaseModel')

    def test_save(self):
        """ sec"""
        N = BaseModel()
        F = N.updated_at
        N.save()
        L = N.updated_at
        self.assertLess(F, L)


if __name__ == "__main__":
    unittest.main()
