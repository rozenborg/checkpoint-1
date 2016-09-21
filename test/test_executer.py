import unittest
import pdb
from app.factories.room_factory import RoomFactory
from app.factories.person_factory import PersonFactory
from app.amity import Amity
from app.executor import Executor


# choosing a concrete class here because oeprations happen driectly on concrete classes
# want to test stuff that actually performs actions, like room and commander!

class ExecuterTest(unittest.TestCase):
    def test_executer_can_add_people_to_room(self):
        amity = Amity()

        room = RoomFactory.create("Moon", 4)
        Amity.add_object_to_dictionary(amity, room)
        Amity.modify_dictionary_element(amity, "room", "000001", "purpose", "office")

        person = PersonFactory.create("fellow", "Femi", 25, "M", wants_residence="Y", level="D1")
        Amity.add_object_to_dictionary(amity, person)

        Executor.assign_occupant_to_room(person, room)
        self.assertIn(person.id, room.occupants)
        self.assertEqual(room.occupant_count, 1)
        self.assertEqual(amity.rooms["000001"].occupants, person)


if __name__ == '__main__':
    unittest.main()
