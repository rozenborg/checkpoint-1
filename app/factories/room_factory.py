from app.room import Room
from app.amity import Amity
import pdb


class RoomFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def create(name, max_occupancy):
        room = Room(name, max_occupancy)

        return room
