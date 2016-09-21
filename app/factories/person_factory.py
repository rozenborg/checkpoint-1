from app.amity import Amity
from app.fellow import Fellow
from app.staff import Staff
import pdb


class PersonFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def create(role, name, age, gender, **kwargs):
        if role.lower() == "fellow":
            wants_residence = kwargs.get("wants_residence")
            level = kwargs.get("level")
            person = Fellow(name, age, gender, wants_residence, level)

        if role.lower() == "staff":
            job_title = kwargs.get("job_title")
            department = kwargs.get("department")
            person = Staff(name, age, gender, job_title, department)

        return person
