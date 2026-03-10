s = "azyxyyzaaaa"
q = ["a", "z", "y", "x"]

hash_list = [0] * 26
for char in s:
    ascii_val = ord(char)
    index = ascii_val - 97
    hash_list[index] += 1

for char in q:
    ascii_val = ord(char)
    index = ascii_val - 97
    print(hash_list[index])