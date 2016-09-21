import unittest
from app.office import Office
from app.living_space import LivingSpace
from app.fellow import Fellow
from app.staff import Staff
from app.factories.room_factory import RoomFactory
from app.room import Room
import pdb


class RoomTestCase(unittest.TestCase):
    def test_assign_room_purpose(self):
        room = RoomFactory.create("Mission Control", 6)
        room.purpose = Room.assign_room_purpose("Mission Control", "office")
        self.assertEqual(room.purpose, "office")

if __name__ == '__main__':
    unittest.main()
