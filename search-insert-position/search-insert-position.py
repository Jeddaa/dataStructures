def SearchInsertPosition(nums, target):
    if not nums:
        return 0
    for i in range(0, len(nums)):
        if (nums[i] == target):
            return i
        if nums[i] > target and i == 0:
            return i
        if nums[i] < target and i == len(nums) - 1:
            return i+1
        if nums[i] > target and nums[i - 1] < target:
            return i


print(SearchInsertPosition([1, 3, 5, 6], 5))
print(SearchInsertPosition([1, 3, 5, 6], 7))
