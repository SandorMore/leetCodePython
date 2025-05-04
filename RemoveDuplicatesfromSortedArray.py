def removeDuplicates(nums) -> int:
    seen = set()
    duplicates = 0

    for num in nums:
        if num in seen:
            duplicates += 1
        else:
            seen.add(num)

    return duplicates

print(removeDuplicates([1, 1, 2])) # Output: 1
        