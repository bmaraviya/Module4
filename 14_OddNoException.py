"""Write python program that user to enter only odd numbers, else will raise an exception."""

try:
    no = int(input("Enter Number:"))
    if no%2==0:
        raise ValueError("This is not Odd Number")
except ValueError as e:
    print(e)