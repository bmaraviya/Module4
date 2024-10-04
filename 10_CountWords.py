"""Write a Python program to count the frequency of words in a file."""

fl = open('stdata.txt','r')
words = 0

for i in fl:
    words+=1
    
print()
