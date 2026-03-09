import math
n1 = 153
n2 = 1634
n3 = 90

def checkArmstrong(n):
    num = n
    result = 0
    l = math.floor(math.log10(n) + 1)

    while (num>0):
        digit = num % 10
        result += math.pow(digit, l)
        num = num // 10
    return n == result

print(checkArmstrong(n1))
print(checkArmstrong(n2))
print(checkArmstrong(n3))