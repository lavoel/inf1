from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.module = []
        self.grades = {}

    def add_module(self,module):
        self.module.append(module.title)
        self.grades[module.title] = module.get_grade()

    def get_list_modules(self):
        print("Modules of Student %s:" % self.name)
        for modules in self.module:
            print(modules)

    def get_grades(self):
        print("Grades of Student %s:" % self.name)
        for modules, grades in self.grades.items():
            print(modules,":", grades)



### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
