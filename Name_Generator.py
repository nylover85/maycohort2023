import random
import string
import sys

def string_generator(size=10, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))
    
department = input("Enter Department: Accounting, Finops, Marketing: ")

if department == "Accounting" or department.lower() == "accounting":
    print("You chose the Accounting department.")
elif department == "Finops":
    print("You chose the Finops department.")
elif department == "Marketing":
    print("You chose the Marketing department.")
else:
    print("Invalid department choice.")

number = int(input("How many do you need?: "))

if number > 0:
    print("Standby.")
else:
    print("Must enter a number greater than zero for the request.")

print("Names generated")

for _ in range(1, number + 1):
    unique_name = department
    EC2_name = unique_name + (":") + string_generator()  # Assuming string_generator() is a function you defined elsewhere.
    print("Instance named:", EC2_name)