from math import sqrt
n1 = 36
n2 = 17

def printAllFactors(n):
    num = n
    results = []

    for i in range (1, int(sqrt(num)) + 1):
        if num % i == 0:
            results.append(i)
            if num // i != i:       # making sure that the OTHER factor is not the same as the FIRST factor (helps with identifying square root numbers)
                results.append(num // i)
    results.sort()
    return results

print(printAllFactors(n1))
print(printAllFactors(n2))
