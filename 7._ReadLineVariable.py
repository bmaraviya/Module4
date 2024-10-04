"""Write a Python program to read a file line by line store it into a variable."""

fl = open('stdata.txt','r')
lines = ""
for i in fl:
    lines += i
print(lines)



