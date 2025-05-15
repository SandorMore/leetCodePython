def insertAtPosition(nums: list[int], target: int) -> int:
    L, R = 0, len(nums) - 1  # Initialize pointers

    if target in nums:
        return nums.index(target)
    if target < nums[L]:
        return 0
    if target > nums[R]:
        return len(nums)

    while L <= R:
        mid = (L + R) // 2

        if nums[mid] == target:  
            return mid
        elif nums[mid] < target: 
            L = mid + 1
        else:  
            R = mid - 1

    return L

print(insertAtPosition([1, 2, 3, 4, 5, 7, 8, 9], 7))  # Output: 2