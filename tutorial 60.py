# Date 30-3-2021

class Employe:
    def __init__(self, fname, lname, salary, contactnumber):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.contactnumber = contactnumber


class Programmer(Employe):
    def __init__(self, fname, lname, salary, contactnumber, experience, language):
        super().__init__(fname, lname, salary, contactnumber)
        self.language = experience
        self.language = language


sumit = Employe("Sumit", "Das", "103000", "8003479539")
rohan = Employe("Rohan", "Singh", "96100", "8003479539")

aman = Programmer("Aman", "Rathore", "200000", "8003479539", "0 Years", "Python\nHtml\nCss\nJavaScript\nC\nC++\nArduino")
harry = Programmer("Harry", "Khan", "320000", "9264175175", "11 Years","Almost All")

print(aman.language)
# print(harry.__dict__)
