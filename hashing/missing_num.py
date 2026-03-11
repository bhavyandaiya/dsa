nums = [3, 0, 1, 2]

def missingNumber(nums):
    nums.sort()
    counter = 0

    for i in range(len(nums)):
        if counter != nums[i]:
            return counter
        counter += 1

    return counter

print(missingNumber(nums))