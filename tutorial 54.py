# Date 30-3-2021

class Student:
    no_of_leaves = 5
    # no_of_leaves is a class variable


harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]
# print(harry.section, larry.subjects)


larry.no_of_leaves = 2
# the upper line of code makes a instence variable which is stored in larry.no_of_leaves
# print(harry.no_of_leaves,larry.no_of_leaves)

print(larry.__dict__)
print(harry.__dict__)


