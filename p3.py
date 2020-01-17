"""
Problem 3.

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# this is a hard one 600851475139 = 523 * 1148855593
# rem = 600851475139

rem = 600851475143
s = 2
res = []

while rem != 1:
    if rem % s == 0:
        rem = rem / s
        res.append(s)
        s = 2
    else:
        s += 1

print(max(res))