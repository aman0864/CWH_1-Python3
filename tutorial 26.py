# Date 18-3-2021

file1 = open("tutorial 26.txt", "r")
content = file1.read()
print(content)
file1.close()
# Note: Do not forget to close a file, it is very important to close a file after it's use is finished
# The upper syntax will help you to read and print a file

print(10*"\n")

file1 = open("tutorial 26.txt", "r")
content = file1.read(30)
print(content)
file1.close()
# The upper syntax will help you to read and print only first 30 characters of the given file

print(10*"\n")

file1 = open("tutorial 26.txt", "r")
print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())
file1.close()
# The upper syntax will help you to read and print only first four lines of the given file


print(10*"\n")

file1 = open("tutorial 26.txt", "r")
print(file1.readlines())
file1.close()
# The upper syntax will help you to read and print lines of the given file in the form of list
