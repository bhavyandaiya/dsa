# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

n = 14

def uglyNumber(n):
    num = n
    if num <= 0:
        return False
    for p in [2, 3, 5]:
        while num % p == 0:
            num = num // p

    return num == 1

print(uglyNumber(n))