"""Write a Python program to read a file line by line and store it into a list"""

fl = open('stdata.txt','r')
lines = fl.readlines()
for i in lines:
    print(i)

mylist = []
fl = open('stdata.txt','r')
for i in fl:
    mylist.append(i)
print(mylist)