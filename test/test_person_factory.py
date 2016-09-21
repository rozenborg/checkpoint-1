import unittest
import pdb
from app.factories.person_factory import PersonFactory
from app.person import Person
from app.fellow import Fellow
from app.staff import Staff
from app.amity import Amity


class PersonFactoryTest(unittest.TestCase):
    # def test_personfactory_can_create_person(self):

    # 	person = PersonFactory.create("Will Smith", 500, "M")
    # 	self.assertIsInstance(person, Person)

    # def test_personfactory_can_create_fellows_and_staff(self):

    # 	person = PersonFactory.create("Bob", 24, "M", "fellow")
    # 	self.assertIsInstance(person, Fellow)

    # 	person = PersonFactory.create("Ashley", 12, "F", "staff")
    # 	self.assertIsInstance(person, Staff)

    # 	person2 = PersonFactory.create("Michael", 26, "M", "staff")
    # 	self.assertIsEqual(person2.id - person1.id, 1)

    # person = Fellow("Name", 25, "M", "Y", "D1")

    # test can create Fellow with residence and level

    # test can create staff with job_title and department

    # tests whether reject invalid inputs
    # one test for levels
    # one test for gender'
    # etc.

    # test whether person is added to dictionary in amity

    # test whether personfactory can create fellow or staff using *args

    # def test_personfactory_can_create_fellow_and_staff_using_kwargs(self):
    #     person = PersonFactory.create("fellow", "Bob", 24, "M", wants_residence="Y", level="D1")
    #     self.assertIsInstance(person, Fellow)
    #
    #     person = PersonFactory.create("staff", "Ashley", 12, "F", job_title="Trainer",
    #                                   department="Learning & Development")
    #     self.assertIsInstance(person, Staff)

    # ^^ this test is passing :)

    # the test below should be an Amity test!

    def test_personfactor_assigns_ordered_id_to_person_when_created(self):
        person = PersonFactory.create("fellow", "Femi", 25, "M", wants_residence="Y", level="D1")
        Amity.add_object_to_dictionary(person)
        self.assertEqual(person.id, "000001")

        person = PersonFactory.create("fellow", "Bob", 26, "Y", wants_residence="N", level="D4")
        self.assertEqual(person.id, "000002")

        person = PersonFactory.create("staff", "Seni", 50, "M", job_title="Director of Operations", department="Operations")
        self.assertEqual(person.id, "000001")

        person = PersonFactory.create("staff", "Michael", 26, "Y", job_title="Trainer", department="Training")
        self.assertEqual(person.id, "000002")

    ## ^^ this test is failing because the program does not yet add people to the dictionary

    # test whether person factory can add people to dictionary in Amity

    # def test_personfactor_can_add_person_to_amity_persondictionary(self):
    #     person1 = PersonFactory.create("fellow", "Femi", 25, "M", wants_residence="Y", level="D2")
    #
    #     person2 = PersonFactory.create("fellow", "Bob", 26, "Y", wants_residence="N", level="D4")
    #     self.assertIn(person1.id, Amity.people)
    #     pdb.set_trace()
    #     self.assertIn(person2.id, Amity.people)

if __name__ == '__main__':
    unittest.main()
