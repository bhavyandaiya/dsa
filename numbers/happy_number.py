n = 13

def isHappy(n, seen = set()):
    result = 0
    while n > 0:
        digit = n % 10
        result += (digit ** 2)
        n = n // 10
    
    if result == 1:
        return True
    
    if result in seen:
        return False
    
    seen.add(result)
    return (isHappy(result, seen))

print(isHappy(n))