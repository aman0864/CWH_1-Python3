# Date 30-3-2021

class Student:
    def __init__(self, fname, lname, previous_year_precentage):
        self.fname = fname
        self.lname = lname
        self.previous_year_precentage = previous_year_precentage

    @classmethod
    def alternative_constructor(cls, string1):
        data = string1.split("-")
        return cls(data[0], data[1], data[2])


aman = Student.alternative_constructor("Aman-Rathore-87.8")
suman = Student.alternative_constructor("Suman-Das-78.5")
rohit = Student.alternative_constructor("Rohit-Sen-63.3")
# print(rohit.__dict__)
# print(aman.__dict__)
# print(suman.__dict__)

print(suman.previous_year_precentage)