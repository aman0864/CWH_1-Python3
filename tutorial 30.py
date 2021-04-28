# Date 19-3-2021

file1 = open("tutorial 30.txt")
print(file1.readline())
print(file1.readline())
print(file1.readline())
print("We are on",file1.tell(),"index number of the given file\n")
file1.seek(5)
print(file1.readline())
print("We are on",file1.tell(),"index number of the given file")
file1.close()