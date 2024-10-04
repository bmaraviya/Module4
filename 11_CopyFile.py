"""Write a Python program to copy the contents of a file to another file."""

fl = open('stdata.txt','r')
nf = open('copyfile.txt','a')
content = fl.read()
nf.write(content)
