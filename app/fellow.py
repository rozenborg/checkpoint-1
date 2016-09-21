from person import Person


class Fellow(Person):
    """A Fellow at Andela

	Attributes:
	level: a string describing which stage of the Fellowship they are in
	wants_residence: a string (y/n) that represents whether or not the Fellow would like to live in Andela housing
	"""
    # level = Level()

    def __init__(self, name, age, gender, wants_residence, level):
        super(Fellow, self).__init__(name, age, gender)
        self.wants_residence = wants_residence
        self.level = level


        # def person_type():
        # 	return Fellow
