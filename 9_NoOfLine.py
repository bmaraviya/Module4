"""Write a Python program to count the number of lines in a text file."""

fl = open('stdata.txt','r')
count = 0

for i in fl:
    count+=1
print(f"The {count} lines in a file")