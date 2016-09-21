from app.room import Room
from app.fellow import Fellow
from app.amity import Amity


class Executor(object):
    def __init__(self):
        pass

    @staticmethod
    def assign_occupant_to_room(person, room):
        room.occupants[person.id] = person
        amity.rooms[room.id] = room
        return amity.rooms

    #come back to this