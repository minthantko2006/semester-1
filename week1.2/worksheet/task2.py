# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
numbers = read_numbers ()
if len(numbers)==0 :
    sys.exit("Error: no numbers provided")
minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)
numbers.sort()
n = len(numbers)
median = n // 2
if n % 2 == 0 :
    median = (numbers[median -1] + numbers[median]) / 2
else:
    median = numbers[median]

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")



