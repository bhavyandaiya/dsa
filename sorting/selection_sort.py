nums = [5, 7, 8, 8, 4, 1, 6, 9, 2]

# ASCENDING:
def selection_sort_asc(nums):
    n = len(nums)
    for i in range(0, n):
        mini_ind = i
        for j in range(i + 1, n):
            if nums[j] < nums[mini_ind]:
                mini_ind = j
        nums[i], nums[mini_ind] = nums[mini_ind], nums[i]
    return nums
print(selection_sort_asc(nums))


# DESCENDING

# nums = [5, 7, 8, 8, 4, 1, 6, 9, 2]
def selection_sort_des(nums):
    n = len(nums)
    for i in range(0, n):
        max_ind = i
        for j in range(i + 1, n):
            if nums[j] > nums[max_ind]:
                max_ind = j
        nums[i], nums[max_ind] = nums[max_ind], nums[i]
    return nums


print(selection_sort_des(nums))