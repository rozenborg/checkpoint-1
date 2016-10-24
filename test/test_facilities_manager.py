# may need to run export PYTHONPATH=$PYTHONPATH:`pwd -P` in the command line before executing tests

import unittest
from app.amity_manager import RoomManager
from app.amity import Amity
from database_writer import DatabaseWriter


class AllTests(unittest.TestCase):
    def test_can_add_people_to_system(self):
        # tests whether you can Fellows and team members to people databases
        # Amity.delete_people()
        Amity.add_person("Bob", "bob@andela.com", "m", "fellow", "D1", "y")
        Amity.add_person("Louis", "louis@andela.com", "f", "staff", "Accountant", "Finance")
        # can query the database to see if we have added people successfully at this point
        # people = Amity.report_people()
        DatabaseWriter.select_from_database("")
        # this is where we see whether the people were added to the database
        # will probably execute a query and then use the assert statements against the query
        assertIn("bob@andela.com", people)
        assertIn("louis@andela.com", people)

    # def test_can_add_rooms_to_system(self):
    #     # tests whether you can add rooms to rooms database
    #     RoomManager.delete_rooms()
    #     addRoom("Orien", 4)
    #     addRoom("Moon", 6)
    #     rooms = reportRooms()
    #     # this is where we see whether the rooms were added to the system
    #
    # def test_can_assign_rooms_purposes(self):
    #     # tests whether you can assign an room a function as an office or living space
    #     RoomManager.delete_rooms()
    #     RoomManager.add_room("Orien", 4)
    #     RoomManager.add_oom("Moon", 6)
    #     RoomManager.assign_room_purpose("Orien", "Office")
    #     RoomManager.assign_room_purpose("Moon", "Living Quarters")
    #     rooms = Amity.reportRooms()
    #     # this is where we see whether the rooms were given purposes
    #     assertEqual(rooms['orien']['purpose'], 'office')
    #     assertEqual(rooms['moon']['purpose'], 'living quarters')
    #
    # def test_can_manually_assign_people_to_rooms(self):
    #     """
    #     tests whether you can add any person to an office
    #     and an interested Fellow but not team member or disinterested Fellow to a living space
    #     and no more than the occupancy of the room
    #     and not multiple different genders to living spaces
    #     """
    #     deleteRooms()
    #     deletePeople()
    #     addRoom("Orien", 2)
    #     addRoom("Moon", 2)
    #     assignRoomPurpose("Orien", "Office")
    #     assignRoomPurpose("Moon", "Living Quarters")
    #     addPerson("Bob", "bob@andela.com", "m", "fellow", "D1", "y")
    #     addPerson("Doug", "doug@andela.com", "m", "fellow", "D0", "y")
    #     addPerson("Louis", "louis@andela.com", "f", "staff", "Accountant", "Finance")
    #     addPerson("Ralph", "ralph@andela.com", "m", "fellow", "D1", "y")
    #     addPerson("Blessing", "blessing@andela.com", "f", "fellow", "D2", "y")
    #     addPerson("Chuck", "check@andela.com", "m", "fellow", "D3", "n")
    #
    #     assignToRoom("Orien", "bob@andela.com", "louis@andela.com")
    #     # this is where we check whether the Fellow and Staff have been added to the office
    #     assignToRoom("Orien", "blessing@andela.com")
    #     # this is where we check whether it raises an error if you assign people past the max occupancy
    #     assignToRoom("Moon", "bob@andela.com", "blessing@andela.com")
    #     # this is where we check whether it raises an error when we try to add multiple genders to the same living quarters
    #     assignToRoom("Moon", "bob@andela.com")
    #     # this is where we check whether bob was successfully added to the living quarters
    #     assignToRoom("Moon", "blessing@andela.com")
    #     # this is where we check whether it raises an error when we try to add female to male room
    #     assignToRoom("Moon", "chuck@andela.com")
    #     # this is where we check whether it raises an error when you try to add someone who is not interested
    #     assignToRoom("Moon", "louis@andela.com")
    #     # this is where we check whether it successfully adds a second person to the living space
    #     assignToRoom("Moon", "ralph@andela.com")
    #     # this is where we check whether it raises an error when you try and surpass the occupancy of a living space
    #
    # def test_can_randomly_assign_people_to_rooms(self):
    #     # can randomly assign every to an office space and interested Fellows to living spaces by gender
    #     Amity.delete_rooms()
    #     deletePeople()
    #     addRoom("Orien", 2)
    #     addRoom("Moon", 2)
    #     assignRoomPurpose("Orien", "Office")
    #     assignRoomPurpose("Moon", "Living Quarters")
    #     addPerson("Bob", "bob@andela.com", "m", "fellow", "D1", "y")
    #     addPerson("Doug", "doug@andela.com", "m", "fellow", "D0", "y")
    #     addPerson("Louis", "louis@andela.com", "f", "staff", "Accountant", "Finance")
    #     addPerson("Ralph", "ralph@andela.com", "m", "fellow", "D1", "y")
    #     addPerson("Blessing", "blessing@andela.com", "f", "fellow", "D2", "y")
    #     addPerson("Chuck", "check@andela.com", "m", "fellow", "D3", "n")
    #     autoAssign()
    #     # checks whether office is full, room either has the lone female or is full with males, and prints unassigned peeps
    #
    # def test_can_print_room_allocations(self):
    #     # can generate a list of all room allocations
    #     deleteRooms()
    #     deletePeople()
    #     addRoom("Orien", 2)
    #     addRoom("Moon", 2)
    #     assignRoomPurpose("Orien", "Office")
    #     assignRoomPurpose("Moon", "Living Quarters")
    #     addPerson("Bob", "bob@andela.com", "m", "fellow", "D1", "y")
    #     addPerson("Doug", "doug@andela.com", "m", "fellow", "D0", "y")
    #     addPerson("Louis", "louis@andela.com", "f", "staff", "Accountant", "Finance")
    #     addPerson("Ralph", "ralph@andela.com", "m", "fellow", "D1", "y")
    #     addPerson("Blessing", "blessing@andela.com", "f", "fellow", "D2", "y")
    #     addPerson("Chuck", "check@andela.com", "m", "fellow", "D3", "n")
    #     autoAssign()
    #     printAllocations()
    #     # ...


if __name__ == '__main__':
    unittest.main()
