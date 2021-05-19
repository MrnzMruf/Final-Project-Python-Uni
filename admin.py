from student import student
from course import Course
from login import User, log_event
import json
import os

"""
Class admin: child of user class
include define course, display student list, check unit students
"""


class admin(User):
    """
    :param: role: admin
    :param: username: username of admin
    :param: password: password of admin
    """

    def __init__(self, role, username, password):
        super().__init__(role, username, password)
        self.name = username

    """
    :param: title: the title of course
    :param: professor: the name of professor who present that course
    :param: unit: the number of unit for each course
    :param: capacity: remain capacity for each course
    :param: major: what is major for each course 
    """

    def define_course(self, title, professor, unit, capacity, major):
        Course.add_course(title, professor, unit, capacity, major)
        Course.save_db()
        log_event(f"{title} course is added")

    def stu_list(self):
        User.stu_list()

    def is_take_any_course(self, stu_name):
        return os.path.exists(f'stu_taken_course\{stu_name + ".json"}')

    def select_student(self, stu_name):
        # student.total_units
        if stu_name in User.student_db['full_name'].values:
            password = User.admin_db[User.admin_db['username'] == self.username]['password'].tolist()[0]
            print(student(stu_name, password))
        else:
            print(f"{stu_name} student is not exist in database")
            return False
        if self.is_take_any_course(stu_name):
            with open(f"stu_taken_course\{stu_name}.json", 'r') as jp:
                d = json.load(jp)
                print('selected courses :')
                print(d)

            return True
        print(" >> Student is not took any courses yet")
        return False

    """
    Check courses and modify that status to accept or not accept 
    """

    def check_stu_units(self, stu_name, accept=True):
        if accept:
            with open(f"stu_taken_course\{stu_name}.json", 'r+') as jp:
                d = json.load(jp)
                tmp = {key: "accepted" for key, _ in d.items()}

            with open(f"stu_taken_course\{stu_name}.json", 'w+') as jp:
                json.dump(tmp, jp)
            log_event(f"{stu_name} took courses are Accepted")
        else:
            with open(f"stu_taken_course\{stu_name}.json", 'r+') as jp:
                d = json.load(jp)
                tmp = {key: "Not-accepted" for key, _ in d.items()}

            with open(f"stu_taken_course\{stu_name}.json", 'w+') as jp:
                json.dump(tmp, jp)
            log_event(f"{stu_name} took courses are not Accepted")


