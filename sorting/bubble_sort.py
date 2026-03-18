nums = [5, 8, 1, 6, 9, 2, 4]

def bubble_sort_asc(nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        swapped = False
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if swapped == False:
            break
    return nums

print(bubble_sort_asc(nums))


def bubble_sort_des(nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        swapped = False
        for j in range(0, i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if swapped == False:
            break
    return nums

print(bubble_sort_des(nums))