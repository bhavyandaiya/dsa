nums = [43, 2, 5, -3, 5, 1, float("inf")]

def func(nums):
    largest = float("-inf")
    n = len(nums)

    for i in range(0, n):
        largest = max(largest, nums[i])
    
    return largest

print(func(nums))