# Date 30-3-2021

class Student:
    def __init__(self, fname, lname, previous_year_precentage):
        self.fname = fname
        self.lname = lname
        self.previous_year_precentage = previous_year_precentage

    @staticmethod
    def good_child(child_name):
        print(child_name+" is a good child.")


aman = Student("Aman", "Rathore", "87.8")
suman = Student("Suman", "Das", "78.5")
rohit = Student("Rohit", "Sen", "63.3")

# print(aman.__dict__)
# good_child("Aman")
aman.good_child(aman.fname)
