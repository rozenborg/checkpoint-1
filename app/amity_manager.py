class RoomManager(object):
    def __init__(self):
        pass

    def delete_rooms(self):
        return delete_from_table(rooms)
