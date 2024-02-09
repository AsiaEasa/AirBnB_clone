#!/usr/bin/python3
"""
    TestReview
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview(unittest.TestCase):
    """the Review class."""

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_new(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_idType(self):
        self.assertEqual(str, type(Review().id))

    def test_createdType(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updatedType(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_args(self):
        esr = Review(None)
        self.assertNotIn(None, esr.__dict__.values())

    def test_placeType(self):
        esr = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(esr))
        self.assertNotIn("place_id", esr.__dict__)

    def test_userType(self):
        esr = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(esr))
        self.assertNotIn("user_id", esr.__dict__)

    def test_textType(self):
        esr = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(esr))
        self.assertNotIn("text", esr.__dict__)

    def test_DReviews(self):
        esr1 = Review()
        esr2 = Review()
        self.assertNotEqual(esr1.id, esr2.id)

    def test_kwargs(self):
        esr = datetime.today()
        dt_iso = esr.isoformat()
        v = Review(id="355", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(v.id, "355")
        self.assertEqual(v.created_at, esr)
        self.assertEqual(v.updated_at, esr)

    def test_DReviewsTime(self):
        esr1 = Review()
        sleep(0.03)
        esr2 = Review()
        self.assertLess(esr1.created_at, esr2.created_at)

    def test_DReviewsUP(self):
        esr1 = Review()
        sleep(0.02)
        esr2 = Review()
        self.assertLess(esr1.updated_at, esr2.updated_at)

    def test_Str(self):
        ee = datetime.today()
        ee_re = repr(ee)
        esr = Review()
        esr.id = "123123"
        esr.created_at = esr.updated_at = ee
        rvstr = esr.__str__()
        self.assertIn("[Review] (123123)", rvstr)
        self.assertIn("'id': '123123'", rvstr)
        self.assertIn("'created_at': " + ee_re, rvstr)
        self.assertIn("'updated_at': " + ee_re, rvstr)

    def test_to_dictarg(self):
        RR = Review()
        with self.assertRaises(TypeError):
            RR.to_dict(None)

    def test_to_dictTYPe(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def testTOsave_arg(self):
        SS = Review()
        with self.assertRaises(TypeError):
            SS.save(None)

    def testNOarg(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str_representation(self):
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great place!"
        str_representation = str(review)
        self.assertIsInstance(str_representation, str)
        self.assertIn("Review", str_representation)
        self.assertIn("123", str_representation)
        self.assertIn("456", str_representation)
        self.assertIn("Great place!", str_representation)

    def testtodict_dunder_dict(self):
        R = Review()
        self.assertNotEqual(R.to_dict(), R.__dict__)

    def test_inequality(self):
        review1 = Review(id="1", place_id="123", user_id="456", text="Great")
        review2 = Review(id="2", place_id="456", user_id="789", text=" place!")
        self.assertNotEqual(review1, review2)

    def test_attributes_assignment(self):
        review = Review()
        review.place_id = "123"
        review.user_id = "123"
        review.text = "Great place!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "123")
        self.assertEqual(review.text, "Great place!")

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
