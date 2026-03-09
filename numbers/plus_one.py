num1 = [9, 2, 3]
num2 = [4, 2, 1]
num3 = [9]

def plusOne(num):
    result = 0
    for i in range(len(num)):
        result = (result * 10) + num[i]
    return list(map(int, str(result + 1)))

num1 = [9, 2, 3]
num2 = [4, 2, 1]
num3 = [9]

print(plusOne(num1))  
print(plusOne(num2))  
print(plusOne(num3)) 