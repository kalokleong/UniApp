import sys
from os import name, system

from common.color import Color
from models.admin import Admin
from models.student import Student

from cli.controllers import admin_controller as admin_ctrl
from cli.controllers import student_controller as stu_ctrl


class UniApp:
    session: Student | Admin | None

    def __init__(self) -> None:
        self.session = None

    def main(self):
        while True:
            if type(self.session) is Admin:
                self.admin_menu()
            elif type(self.session) is Student:
                self.student_menu()
            else:
                self.default_menu()

    def default_menu(self):
        while True:
            userchoice = input(
                "\033[36mUniversity System: (A)dmin, (S)tudent, or X : \033[0m"
            )

            match userchoice:
                case "a" | "A":
                    self.session = Admin()
                    break
                case "s" | "S":
                    self.student_login()
                    break
                case "x" | "X":
                    Color.prYellow("Thank You")
                    self.exit()
                    break

    def admin_menu(self):
        while True:
            userchoice = input("\033[36m\tAdmin System (c/g/p/r/s/x): \033[0m")

            match userchoice.lower():
                case "c":
                    admin_ctrl.AdminController().clear_database()
                case "g":
                    admin_ctrl.AdminController().view_by_grade()
                case "p":
                    admin_ctrl.AdminController().view_by_passfail()
                case "r":
                    admin_ctrl.AdminController().remove_student()
                case "s":
                    admin_ctrl.AdminController().view_students()
                case "x":
                    self.__logout()
                    break

    def student_login(self):
        while True:
            userchoice = input("\033[36m\tStudent System (l/r/x): \033[0m")

            match userchoice.lower():
                case "l":
                    student = stu_ctrl.StudentController().login()
                    if student:
                        self.session = student
                        break
                case "r":
                    stu_ctrl.StudentController().register()
                case "x":
                    break

    def student_menu(self):
        while True:
            if type(self.session) is not Student:
                break

            userchoice = input("\033[36m\t\tStudent Course Menu (c/e/r/s/x) : \033[0m")

            match userchoice.lower():
                case "c":
                    stu_ctrl.StudentController().change_password(self.session)
                case "e":
                    stu_ctrl.StudentController().enrol_subject(self.session)
                case "r":
                    stu_ctrl.StudentController().remove_subject(self.session)
                case "s":
                    stu_ctrl.StudentController().view_enrolment(self.session)
                case "x":
                    self.__logout()
                    break

    def __logout(self):
        self.session = None

    @staticmethod
    def clear():
        # for windows
        if name == "nt":
            _ = system("cls")
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system("clear")

    @staticmethod
    def exit():
        sys.exit()