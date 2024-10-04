"""Write a Python program to read last n lines of a file."""

fl = open('stdata.txt','r')

print(fl.readlines()[-1])