def RemoveDuplicates(nums):
    if not nums:
        return 0
    j = 1
    for i in range(1, len(nums)):
        if (nums[i] != nums[i-1]):
            nums[j] = nums[i]
            j = j+1
    print(nums)
    return j


print(RemoveDuplicates([1, 1, 2]))
print(RemoveDuplicates([1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10]))
