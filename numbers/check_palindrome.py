n1 = 1234
n2 = 12321

def checkPalindrome(n):
    num = n
    result = 0

    while (num>0):
        digit = num % 10
        result = (result * 10) + digit
        num = num // 10

    return n == result

print(checkPalindrome(n1))
print(checkPalindrome(n2))
