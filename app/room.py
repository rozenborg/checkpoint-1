class Room(object):
    def __init__(self, name, max_occupancy):
        self.name = name
        self.max_occupancy = max_occupancy
        self.occupants = {}
        self.occupant_count = 0
        self.purpose = ''
