# Date 30-3-2021

class Student:
    def __init__(self, fname, lname, previrios_year_precentage):
        self.fname = fname
        self.lname = lname
        self.previrios_year_precentage = previrios_year_precentage

    def details(self):
        return f"Student first name is {self.fname}\nStudent last name is {self.lname}\nStudent previrios year precentage is {self.previrios_year_precentage}"


aman = Student("Aman", "Rathore", "88.7")
# print(aman.__dict__)
print(aman.details())
