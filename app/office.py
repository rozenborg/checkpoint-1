from room import Room

class Office(Room):
	"""A room which is suitable to be used as an office 

	Attributes:
	"""
	def __init__(self, name, max_occupancy):

		super(Office, self).__init__(name, max_occupancy)


