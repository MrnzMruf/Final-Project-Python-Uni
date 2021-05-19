from os import name
from login import User
from student import student
from admin import admin
from colorama import Fore, Back, Style
import logging

"""
Main page include login with admin and student
"""
mylogger = logging.getLogger("loger1")
file_handeler_event = logging.FileHandler('file_event.log')
std_handeler = logging.StreamHandler()
file_handeler_event.setLevel(logging.INFO)
std_handeler.setLevel(logging.ERROR)
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                               datefmt='%Y-%m-%d %H:%M:%S')
file_handeler_event.setFormatter(log_format)
mylogger.addHandler(file_handeler_event)
mylogger.addHandler(std_handeler)


class App:

    def __init__(self):
        self.user = None

    @staticmethod
    def first_page():
        print(Fore.MAGENTA + '[1] Login\n[q] Quit')
        print(Style.RESET_ALL)
        return input('>>> please Select a choice :')

    def login_page(self):
        print(Fore.MAGENTA + "____Login____")
        print(Fore.LIGHTBLUE_EX + '  |  [1] admin\n  |  [2] student ')
        print(Style.RESET_ALL)
        r = input('  |__please select a role  : ')
        user_name = input('  |__please enter your user name : ')
        password = input('  |__please enter your password : ')

        if r == '1':
            self.user = admin('admin', user_name, password)
        elif r == '2':
            self.user = student(user_name, password)
        else:
            mylogger.error("role incorrect!")
            print(Fore.RED + 'wrong role selected')
            print(Style.RESET_ALL)
            return
        return self.user.login()

    def admin_page(self):
        while True:
            print(Fore.MAGENTA + "________ Admin ________")
            print(Fore.LIGHTBLUE_EX + '  | [1] add course')
            print(Fore.LIGHTBLUE_EX + '  | [2] students List')
            print(Fore.LIGHTBLUE_EX + '  | [3] select student')
            print(Fore.LIGHTBLUE_EX + "  | [q] log out")
            print(Style.RESET_ALL)
            user_input = input('  |__please select a choice  : ')
            if user_input == 'q':
                self.user.logout()
                break
            elif user_input == '1':
                title = input('title : ')
                professor = input('professor : ')
                unit = input('unit : ')
                capacity = input('capacity : ')
                major = input('major : ')
                self.user.define_course(title, professor, unit, capacity, major)
            elif user_input == '2':
                self.user.stu_list()
            elif user_input == '3':
                name = input('  |__please enter student name : ')
                r = self.user.select_student(name)
                if r:
                    print("___")
                    print(Fore.LIGHTBLUE_EX + '  |_[1] accept units')
                    print(Fore.LIGHTBLUE_EX + '  |_[2] Not-accept units')
                    print(Fore.LIGHTBLUE_EX + '  |_[3] back')
                    print(Style.RESET_ALL)
                    user_input = input('  |__please select a choice  : ')
                if user_input == '1':
                    self.user.check_stu_units(name, accept=True)
                elif user_input == '2':
                    self.user.check_stu_units(name, accept=False)

    def student_page(self):
        while True:
            print(Fore.MAGENTA + "________ student ________")
            print(Style.RESET_ALL)
            print(Fore.LIGHTBLUE_EX + '  | [1] display courses')
            print(Fore.LIGHTBLUE_EX + '  | [2] choose course')
            print(Fore.LIGHTBLUE_EX + '  | [3] display taken courses')
            print(Fore.LIGHTBLUE_EX + "  | [q] log out")
            print(Style.RESET_ALL)
            user_input = input('  |__please select a choice  : ')
            if user_input == 'q':
                self.user.logout()
                break
            elif user_input == '1':
                self.user.display_course()
            elif user_input == '2':
                course_title = input('Enter course title :')
                self.user.choose_course(course_title)
            elif user_input == '3':
                self.user.display_taken_course()



break_flag = True
while break_flag:
    user_input = App.first_page()
    if user_input == 'q':
        break_flag = False
    elif user_input == '1':
        app = App()
        if app.login_page():
            if app.user.role == 'admin':
                app.admin_page()
            elif app.user.role == 'student':
                app.student_page()
