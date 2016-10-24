import pdb
from database import setup


class Amity(object):

    def __init__(self):
        # run setup here
        setup.create_db()
        pass

    def delete_rooms(self):
        pass

    def delete_people(self):


'''everything below this line is old :)'''

    # def __init__(self):
    #     self.people = {
    #         # "test": 1  # this is only to simulate a full dictionary for testing purposesq
    #     }
    #     # these are object properties, so they only come into being if the class is instantiated
    #     # need them to be class variables for them to be callable in the assign_id function below
    #
    #     self.rooms = {
    #
    #     }
    #
    # def add_object_to_dictionary(self, object):
    #     dictionary = self.rooms if 'room' in str(object.__class__) else self.people
    #     object.id = self.assign_id(object)
    #     dictionary[object.id] = object
    #     return dictionary
    #
    # def assign_id(self, object):
    #
    #     dictionary = self.rooms if 'room' in str(object.__class__) else self.people
    #     # pdb.set_trace()
    #     if not dictionary:
    #         object.id = 1
    #
    #     else:
    #         object.id = len(dictionary) + 1
    #
    #     return '%06d' % object.id  # this won't work in python 3
    #
    # def modify_dictionary_element(self, object_type, key, change_variable, new_value):
    #     dictionary = self.rooms if object_type == 'room' else self.people
    #     setattr(dictionary[key], change_variable, new_value)
    #     return dictionary
    #
    # def assign_occupant_to_room(self, person, room):
    #     # pdb.set_trace()
    #     room.occupants[person.id] = person
    #     room.occupant_count = len(room.occupants)
    #     self.rooms[room.id] = room
    #     return self.rooms
