# nums = [3, 9, 5, 6, 7, 2]
# k = 3

# def right_rotate(nums, k):
#     while (k > 0):
#         n = len(nums)
#         temp = nums[n-1]

#         for i in range(n-2, -1, -1):
#             nums[i + 1] = nums[i]
#         nums[0] = temp

#         k -= 1
    
#     return nums

# print(right_rotate(nums, k))

# Optimal Solution (Reversing)

nums = [3, 9, 5, 6, 7, 2, 10, 9]
k = 5
n = len(nums)

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
reverse(nums, n-k, n-1)
reverse(nums, 0, n-k-1)
reverse(nums, 0, n-1)

print(nums)
