n = [5, 1, 2, 6, 7, 3, 5, 5, 2, 1, 7, 6, 4, 10, 10]
m = [6, 23, 6754, 3, 64, 7, 9]

# HASH LIST METHOD:

# def mAndN(n, m):
#     hash_list = [0] * 11
#     for num in n:
#         hash_list[num] += 1
    
#     for num in m:
#         if num < 1 or num > 10:
#             print(f"{num} comes 0 times\n")
#         else:
#             print(f"{num} comes {hash_list[num]} times\n")
        
# mAndN(n, m)

# DICTIONARY METHOD:

freq_dict = {}
for num in n:
    freq_dict[n[num]] = freq_dict.get(num, 0) + 1

for num in m:
    if num < 1 or num > 10:
        print(f"{num} comes 0 times")
    else:
        print(f"{num} comes {freq_dict.get(num, 0)} times")