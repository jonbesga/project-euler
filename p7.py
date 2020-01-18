"""
Problem 7.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

primes_found = []
n = 2


while len(primes_found) < 10001:
    is_prime = True
    for x in range(n, 0, -1):
        if x not in [1, n] and n % x == 0:
            is_prime = False
            break

    if is_prime:
        primes_found.append(n)
    n += 1


print(primes_found[-1])
