"""Write a python program to find the longest words."""

fl = open('stdata.txt','r')
max_words = ""

for i in fl:
    if len(i) > len(max_words):
        max_words = i
print(max_words)