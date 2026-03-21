nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(nums):
    n = len(nums)
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            return False
        
    return True

print(func(nums))