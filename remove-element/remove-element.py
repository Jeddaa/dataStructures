def RemoveElement(nums, val):
    if not nums:
        return 0
    j = 0
    for i in range(0, len(nums)):
        if (nums[i] != val):
            nums[j] = nums[i]
            j = j+1
    print(nums)
    return j


print(RemoveElement([3, 2, 2, 3], 3))
print(RemoveElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
