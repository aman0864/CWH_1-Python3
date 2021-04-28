# Date 18-3-2021

file1 = open("tutorial 28.1.txt", "w")
file1.write("My name is Aman Rathore")
file1.close()
# The upper syntax will overwrite the lines in the given file

print(10*"\n")

file1 = open("tutorial 28.2.txt", "a")
file1.write("My name is Aman Rathore\n")
file1.close()
# The upper syntax will add the lines in the given file(Without losing the previous data)

print(10*"\n")

file1 = open("tutorial 28.3.txt", "r+")
print(file1.read())
a = file1.write("\nMy name is Aman Rathore")
print("\n")
print(a)
# The upper line will help you to know that how many characters you are printing
file1.close()
# The upper syntax will help you toread and write on in the given file at a same time 

# print(10*"\n")
# print(len("My name is Aman Rathore\n"))
