s = "Bhavyan"
l = "nitin"

def func(string, left, right):
    if (left > right):
        return True
    if (string[left] != string[right]):
        return False
    
    return func(string, left + 1, right - 1)




print(func(s, 0, len(s) - 1))
print(func(l, 0, len(l) - 1))