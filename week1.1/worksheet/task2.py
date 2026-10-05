"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Min Thant Ko
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
try:    
    saving_amount = int(input("How much money do you want to save every month? : "))
# Validate that they have entered an integer.

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
    Total_saving_amount_yearly = saving_amount * 12
# print this out for the user with a suitable message.
    print(f"The total amount of money you will save at the end of the year is £{Total_saving_amount_yearly} ")
# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
    With_interest = 0.008*Total_saving_amount_yearly
    Total = Total_saving_amount_yearly + With_interest
# print this out in the format £X.XX (to two decimal places).
    print(f"Including the interest, You will save £{Total:.2f} per year")
except ValueError:
    print("Invalid amount")