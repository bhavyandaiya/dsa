nums = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(nums)

# Slicing method:
# nums[:] = [nums[-1]] + nums[0:n-1]
# print(nums)

# Slicing method (without negative indices):
# nums[:] = [nums[n-1]] + nums[0:n-1]
# print(nums)

# Without slicing (uses temp)

temp = nums[n-1]

for i in range(n-2, -1, -1):
    nums[i + 1] = nums[i]
nums[0] = temp

print(nums)