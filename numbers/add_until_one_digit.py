n = 99999999999999901

def addDigits(num):
    if num == 0 :
        return 0
    return 1 + (n-1) % 9
    


print(addDigits(n))