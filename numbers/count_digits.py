import math
n = 5438

def count_digits(n):
    return math.floor(math.log10(n)) + 1

print(count_digits(n))