"""
Problem 1.

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Useful hint: Numbers are divisible by 3 if the sum of all the individual digits is evenly divisible by 3. For example, the sum of the digits for the number 3627 is 18, which is evenly divisible by 3 so the number 3627 is evenly divisible by 3.
"""

# one-liner
print(sum([n for n in range(1, 1000) if n % 5 == 0 or sum([int(x) for x in str(n)]) % 3 == 0]))
