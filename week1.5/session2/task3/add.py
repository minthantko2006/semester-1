# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum
from money import Money

money1 = Money(1, 99)
money2 = Money(0, 5)

print(money1)
print(money2)

total = money1 + money2
print(total)