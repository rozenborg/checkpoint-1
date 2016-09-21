from person import Person

class Staff(Person):
	"""A person who is a staff member at Andela

	Attributes:
	department: a string representing the department the staff member belongs to
	
	"""
	def __init__(self, name, age, gender, job_title, department):
		# self.name = name
		# self.age = age
		# self.gender = gender
		super(Staff, self).__init__(name, age, gender)
		self.job_title = job_title
		self.department = department