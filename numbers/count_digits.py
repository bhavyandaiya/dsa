n = 5873

def count_digits(n):
    num= n
    c= 0
    while num>0:
        c+= 1
        num= num//10
    print(c)

print(count_digits(n))