nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Brute force Solution:
# def func(nums):
#     largest = float("-inf")
#     s_largest = float("-inf")
#     n = len(nums)

#     for i in range(0, n):
#         largest = max(largest, nums[i])

#     for i in range(0, n):
#         if nums[i] > s_largest and nums[i] != largest:
#             s_largest = nums[i]
    
#     return s_largest

# print(func(nums))



# Optimal Solution: Loop only runs ONCE
def func(nums):
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(nums)

    for i in range(0, n):
        if nums[i] > largest:
            s_largest = largest
            largest = nums[i]
        
        elif nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]

    return s_largest

print(func(nums))