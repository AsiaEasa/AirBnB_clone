#!/usr/bin/python3
"""place """

import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """the Place class."""

    def test_no(self):
        self.assertEqual(Place, type(Place()))

    def test_new_in(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_idType(self):
        self.assertEqual(str, type(Place().id))

    def test_createdType(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updatedType(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_default_values(self):
        ee = Place()
        self.assertEqual(ee.number_rooms, 0)
        self.assertEqual(ee.number_bathrooms, 0)
        self.assertEqual(ee.max_guest, 0)
        self.assertEqual(ee.price_by_night, 0)
        self.assertEqual(ee.latitude, 0.0)
        self.assertEqual(ee.longitude, 0.0)
        self.assertEqual(ee.amenity_ids, [])

    def test_cityPL(self):
        YO = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(YO))
        self.assertNotIn("city_id", YO.__dict__)

    def test_args_unused(self):
        p = Place(None)
        self.assertNotIn(None, p.__dict__.values())

    def test_instantiation_with_kwargs(self):
        eee = datetime.today()
        es = eee.isoformat()
        pl = Place(id="345", created_at=es, updated_at=es)
        self.assertEqual(pl.id, "345")
        self.assertEqual(pl.created_at, eee)
        self.assertEqual(pl.updated_at, eee)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_cont(self):
        p = Place()
        self.assertNotEqual(p.to_dict(), p.__dict__)

    def test_dict(self):
        p = Place()
        with self.assertRaises(TypeError):
            p.to_dict(None)

    def test_placesunique(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_one_save(self):
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    def test_two_saves(self):
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        second_updated_at = pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pl.save()
        self.assertLess(second_updated_at, pl.updated_at)

    def test_Dplaces(self):
        PP = Place()
        sleep(0.03)
        PP2 = Place()
        self.assertLess(PP.created_at, PP2.created_at)

    def test_Dupdated_at(self):
        PP = Place()
        sleep(0.03)
        PP2 = Place()
        self.assertLess(PP.updated_at, PP2.updated_at)

    def test_userID(self):
        YO = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(YO))
        self.assertNotIn("user_id", YO.__dict__)

    def test_namePU(self):
        YO = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(YO))
        self.assertNotIn("name", YO.__dict__)

    def test_Nrooms(self):
        eee = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(eee))
        self.assertNotIn("number_rooms", eee.__dict__)

    def test_Nbathrooms(self):
        eee = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(eee))
        self.assertNotIn("number_bathrooms", eee.__dict__)

    def test_descrType(self):
        YO = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(YO))
        self.assertNotIn("desctiption", YO.__dict__)

    def test_no_args_instantiates(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attributes_assignment(self):
        place = Place()
        place.city_id = "312"
        place.user_id = "123"
        place.name = "Twins Cafee"
        self.assertEqual(place.city_id, "312")
        self.assertEqual(place.user_id, "123")
        self.assertEqual(place.name, "Twins Cafee")


if __name__ == "__main__":
    unittest.main()
