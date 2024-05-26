print("Enter File Name:  ")
fname = input()
print("file created.")

f = open(str(fname), "w")
f.write("#include <stdio.h>")
f.close

f = open("file.c", "r")
print(f.read())