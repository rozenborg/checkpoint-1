from person import Person

class Level(object):

	def __get__(self, instance, value):
		return self.instance

	def __set__(self, instance, value):
		if value.lower() not in ['d1', 'd2', 'd3','d4']:
			raise ValueError('Set Fellow level to D1, D2, D3, or D4.')

		#later we can use a loop so that this fails gracefully, instead of breaking program

		self.instance = value


class Fellow(Person):
	"""A Fellow at Andela

	Attributes:
	level: a string describing which stage of the Fellowship they are in
	wants_residence: a string (y/n) that represents whether or not the Fellow would like to live in Andela housing
	"""
	level = Level()

	def __init__(self, name, age, gender, wants_residence, level):

		super(Fellow, self).__init__(name, age, gender)
		self.wants_residence = wants_residence
		self.level = level

print Fellow("bob", 18, "M", "Y", "D1")
print Fellow("bob", 18, "M", "Y", "fail")