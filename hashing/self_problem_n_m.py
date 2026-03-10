n = [5, 1, 2, 6, 7, 3, 5, 5, 2, 1, 7, 6, 4, 10, 10]
m = [6, 23, 6754, 3, 64, 7]

def mAndN(n, m):
    hash_list = [0] * 11
    for num in n:
        hash_list[num] += 1
    
    for num in m:
        if num < 1 or num > 10:
            print(f"{num} comes 0 times\n")
        else:
            print(f"{num} comes {hash_list[num]} times\n")
        
mAndN(n, m)