"""
Problem 4.

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def check_palindromic(n):
    # I first did ''.join(reversed(n)) and then found a more beautiful way
    return True if str(n)[::-1] == str(n) else False


def p4():
    highest = 0
    for n in range(999, 100, -1):
        for m in range(999, 100, -1):
            if check_palindromic(n * m) and n * m > highest:
                highest = n * m
    return highest


def p4_norp():
    tested = set()
    highest = 0
    for n in range(999, 100, -1):
        for m in range(999, 100, -1):
            if (n, m) not in tested:
                if check_palindromic(n * m) and n * m > highest:
                    highest = n * m
            tested.add((n, m))
            tested.add((m, m))
    return highest

print(p4())

# Performance between checking and no checking duplicate operations.
# Checking duplicated operations is more costly than not
# Example: 
# p4 3.795115386001271
# p4_norp 9.83570228499957
# 
# from timeit import timeit
# print('p4', timeit("p4()", setup="from __main__ import p4", number=10))
# print('p4_norp', timeit("p4_norp()", setup="from __main__ import p4_norp", number=10))
