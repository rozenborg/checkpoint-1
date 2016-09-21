import unittest
from app.amity import Amity
from app.factories.person_factory import PersonFactory
from app.factories.room_factory import RoomFactory
import pdb

class AmityTest(unittest.TestCase):

    # def test_amity_can_add_people_to_dictionary_with_ids(self):
    #     amity = Amity()
    #
    #     person = PersonFactory.create("fellow", "Femi", 25, "M", wants_residence="Y", level="D1")
    #     Amity.add_object_to_dictionary(amity, person)
    #     self.assertEqual(person.id, "000001")
    #
    #     person = PersonFactory.create("fellow", "Bob", 26, "Y", wants_residence="N", level="D4")
    #     Amity.add_object_to_dictionary(amity, person)
    #     self.assertEqual(person.id, "000002")
    #
    #     person = PersonFactory.create("staff", "Seni", 50, "M", job_title="Director of Operations",
    #                                   department="Operations")
    #     Amity.add_object_to_dictionary(amity, person)
    #     self.assertEqual(person.id, "000003")
    #
    #     person = PersonFactory.create("staff", "Michael", 26, "Y", job_title="Trainer", department="Training")
    #     Amity.add_object_to_dictionary(amity, person)
    #     self.assertEqual(person.id, "000004")
    #
    #     self.assertIn("000001", amity.people)
    #     self.assertIn("000002", amity.people)
    #     self.assertIn("000003", amity.people)
    #     self.assertIn("000004", amity.people)
    #
    # # ^^ this is passing :) :)
    #
    # def test_amity_can_add_rooms_to_dictionary_with_ids(self):
    #     amity = Amity()
    #
    #     room = RoomFactory.create("Moon", 4)
    #     Amity.add_object_to_dictionary(amity, room)
    #     self.assertEqual(room.id, "000001")
    #
    #     room = RoomFactory.create("Jupiter", 6)
    #     Amity.add_object_to_dictionary(amity, room)
    #     self.assertEqual(room.id, "000002")
    #
    #     self.assertIn("000001", amity.rooms)
    #     self.assertIn("000002", amity.rooms)
    #
    #     # ^^ this is passing :) :)
    #
    # def test_amity_can_add_both_rooms_and_people_to_separate_dictionaries(self):
    #     amity = Amity()
    #
    #     room = RoomFactory.create("Moon", 4)
    #     Amity.add_object_to_dictionary(amity, room)
    #     self.assertEqual(room.id, "000001")
    #
    #     room = RoomFactory.create("Jupiter", 6)
    #     Amity.add_object_to_dictionary(amity, room)
    #     self.assertEqual(room.id, "000002")
    #
    #     person = PersonFactory.create("fellow", "Femi", 25, "M", wants_residence="Y", level="D1")
    #     Amity.add_object_to_dictionary(amity, person)
    #     self.assertEqual(person.id, "000001")
    #
    #     person = PersonFactory.create("fellow", "Bob", 26, "Y", wants_residence="N", level="D4")
    #     Amity.add_object_to_dictionary(amity, person)
    #     self.assertEqual(person.id, "000002")
    #
    #     person = PersonFactory.create("staff", "Seni", 50, "M", job_title="Director of Operations",
    #                                   department="Operations")
    #     Amity.add_object_to_dictionary(amity, person)
    #     self.assertEqual(person.id, "000003")
    #
    #     person = PersonFactory.create("staff", "Michael", 26, "Y", job_title="Trainer", department="Training")
    #     Amity.add_object_to_dictionary(amity, person)
    #     self.assertEqual(person.id, "000004")
    #
    #     self.assertIn("000001", amity.people)
    #     self.assertIn("000002", amity.people)
    #     self.assertIn("000003", amity.people)
    #     self.assertIn("000004", amity.people)
    #     self.assertIn("000001", amity.rooms)
    #     self.assertIn("000002", amity.rooms)

        # ^^ this is passing :) :)

    # def test_amity_can_use_modifydictionaryelement_to_change_room_purpose(self):
    #     amity = Amity()
    #
    #     room = RoomFactory.create("Moon", 4)
    #     Amity.add_object_to_dictionary(amity, room)
    #     self.assertEqual(room.id, "000001")
    #
    #     room = RoomFactory.create("Jupiter", 6)
    #     Amity.add_object_to_dictionary(amity, room)
    #     self.assertEqual(room.id, "000002")
    #
    #     Amity.modify_dictionary_element(amity, "room", "000001", "purpose", "office")
    #     self.assertEqual(amity.rooms["000001"].purpose, "office")

        # ^^ this is passing :) :)

    # def test_amity_can_use_modifydictionaryelement_to_change_fellow_wantresidency(self):
    #     amity = Amity()
    #
    #     person = PersonFactory.create("fellow", "Femi", 25, "M", wants_residence="Y", level="D1")
    #     Amity.add_object_to_dictionary(amity, person)
    #
    #     Amity.modify_dictionary_element(amity, "person", "000001", "wants_residence", "N")
    #     self.assertEqual(amity.people["000001"].wants_residence, "N")

        # ^^ this is passing :) :)

    def test_amity_can_add_people_to_room(self):
        amity = Amity()

        room = RoomFactory.create("Moon", 4)
        Amity.add_object_to_dictionary(amity, room)
        Amity.modify_dictionary_element(amity, "room", "000001", "purpose", "office")

        person1 = PersonFactory.create("fellow", "Femi", 25, "M", wants_residence="Y", level="D1")
        Amity.add_object_to_dictionary(amity, person1)

        Amity.assign_occupant_to_room(amity, person1, room)

        person2 = PersonFactory.create("staff", "Bob", 20, "F", job_title="Facilitator", department="Learning and Development")
        Amity.add_object_to_dictionary(amity, person2)

        Amity.assign_occupant_to_room(amity, person2, room)

        self.assertIn(person1.id, room.occupants)
        self.assertIn(person2.id, room.occupants)
        # pdb.set_trace()
        self.assertEqual(room.occupant_count, 2)
        self.assertEqual(amity.rooms["000001"].occupants, {'000001': person1, '000002': person2})

    # ^^ this is passing :) :)


if __name__ == '__main__':
    unittest.main()