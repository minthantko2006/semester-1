"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Min Thant Ko
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

try:
    saving_amount = int(input("How much money do you want to save every month? : "))
    Total_saving_amount_yearly = saving_amount * 12
    print(f"The total amount of money you will save at the end of the year : {Total_saving_amount_yearly} ")
    With_interest = 0.8/100*Total_saving_amount_yearly
    Total = Total_saving_amount_yearly + With_interest
    print(f"Including the interest, You will save {Total:.2f} per year")
except ValueError:
    print("Invalid amount")