"""
Problem 5.

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


# Original solution. Takes more time than I would like
# Optimal solution in https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution

x = 1

while True:
    divisible = True
    for n in range(1, 20 + 1):
        if x % n != 0:
            divisible = False
            break
    if not divisible:
        x += 1
        continue
    break

print(x)

