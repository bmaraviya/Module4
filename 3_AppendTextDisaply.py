"""Write a Python program to append text to a file and display the text."""

fl = open('test.txt','a')

n = int(input("Enter How many Student?:"))

for i in range(n):
    id = int(input("Enter Id:"))
    name = input("Enter Your Name:")
    city = input("Enter Your City:")

    fl.write(f"Id={id}\nName={name}\nCity={city}\n")
    print("")

fl = open('test.txt','r')
print(fl.read())
