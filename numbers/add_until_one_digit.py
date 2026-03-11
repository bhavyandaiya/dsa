n = 38

# if n % 10 == 0 -> it's a 1 digit number


def addDigits(num):
    result = 0

    while num > 0:
        digit = num % 10
        result = (result) + digit
        num = num // 10
    
    if len(list(map(int, str(result)))) == 1:
        return result
    else:
        return addDigits(result)

    


print(addDigits(n))