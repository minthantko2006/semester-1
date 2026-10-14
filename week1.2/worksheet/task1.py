# Worksheet 1.2: Task 1 Solution
import sys

User_Grade = input("Enter your grade : ")

if not User_Grade.isdecimal():
    sys.exit("Error: Grade must be an interger between 0 and 100")

User_Grade = int(User_Grade)
if User_Grade > 100:
    sys.exit("Error: Grade must be an interger between 0 and 100")

if 70 <= User_Grade <= 100 :
    print(f"{User_Grade} is a Distinction")
elif 40 <= User_Grade <= 69 :
    print(f"{User_Grade} is a Pass")
elif  0 <= User_Grade <= 39 :
    print(f"{User_Grade} is a Fail")