#!/usr/bin/python3
"""
Unittest classe
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """testing."""

    def testNOargs(self):
        self.assertEqual(User, type(User()))

    def testISpublic_str(self):
        self.assertEqual(str, type(User().id))

    def testCreaATdatetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def testnewStorINobj(self):
        self.assertIn(User(), models.storage.all().values())

    def testSTRrepr(self):
        DD = datetime.today()
        DT = repr(DD)
        us = User()
        us.id = "123123"
        us.created_at = us.updated_at = DD
        U = us.__str__()
        self.assertIn("[User] (123123)", U)
        self.assertIn("'id': '123123'", U)
        self.assertIn("'created_at': " + DT, U)
        self.assertIn("'updated_at': " + DT, U)

    def test_save_with_arg(self):
        yu = User()
        with self.assertRaises(TypeError):
            yu.save(None)

    def test_contrast(self):
        yu = User()
        self.assertNotEqual(yu.to_dict(), yu.__dict__)

    def test_dict(self):
        yu = User()
        with self.assertRaises(TypeError):
            yu.to_dict(None)

    def test_save(self):
        yu = User()
        sleep(0.05)
        first_updated_at = yu.updated_at
        yu.save()
        self.assertLess(first_updated_at, yu.updated_at)

    def test_noargs(self):
        YY = User()
        self.assertIsInstance(YY, User)
        self.assertEqual(YY.email, "")
        self.assertEqual(YY.password, "")
        self.assertEqual(YY.first_name, "")
        self.assertEqual(YY.last_name, "")

    def test_userA(self):
        us = User()
        self.assertTrue(hasattr(us, "email"))
        self.assertTrue(hasattr(us, "password"))
        self.assertTrue(hasattr(us, "first_name"))
        self.assertTrue(hasattr(us, "last_name"))

    def test_userAI(self):
        user = User(
            email="john@example.com",
            password="pass123",
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.password, "pass123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def testEmailPblic(self):
        self.assertEqual(str, type(User.email))

    def testPass(self):
        self.assertEqual(str, type(User.password))

    def testFirst_name(self):
        self.assertEqual(str, type(User.first_name))

    def test_Unique(self):
        U1 = User()
        U2 = User()
        self.assertNotEqual(U1.id, U2.id)

    def test_UPdated_at(self):
        self.assertEqual(datetime, type(User().updated_at))

    def testLAstname(self):
        self.assertEqual(str, type(User.last_name))

    def test_defval(self):
        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")

    def testDIfferent_createdAt(self):
        U1 = User()
        sleep(0.03)
        U2 = User()
        self.assertLess(U1.created_at, U2.created_at)

    def testUserDIFferent_updatedAT(self):
        U1 = User()
        sleep(0.01)
        U2 = User()
        self.assertLess(U1.updated_at, U2.updated_at)

    def test_args_unused(self):
        us = User(None)
        self.assertNotIn(None, us.__dict__.values())

    def testINkwargs(self):
        D = datetime.today()
        IS = D.isoformat()
        us = User(id="123", created_at=IS, updated_at=IS)
        self.assertEqual(us.id, "123")
        self.assertEqual(us.created_at, D)
        self.assertEqual(us.updated_at, D)

    def testINone_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_user_attributes(self):
        user = User(
            email="YUSRA@example.com",
            password="password123",
            first_name="YUSRA",
            last_name="Smith",
        )
        user_dict = user.to_dict()
        self.assertEqual(user_dict["email"], "YUSRA@example.com")
        self.assertEqual(user_dict["password"], "password123")
        self.assertEqual(user_dict["first_name"], "YUSRA")
        self.assertEqual(user_dict["last_name"], "Smith")


if __name__ == "__main__":
    unittest.main()
