def SortColors(nums):
    for i in range(nums):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums