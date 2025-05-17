def two_pointer_example(nums: list[int], target: int) -> bool:
    # Declare two pointers
    L, R = 0, len(nums) - 1  # L starts at the beginning, R starts at the end

    while L < R:  # Continue until the pointers meet
        current_sum = nums[L] + nums[R]
        
        if current_sum == target:  # If the sum matches the target
            return True
        elif current_sum < target:  # If the sum is too small, move L to the right
            L += 1
        else:  # If the sum is too large, move R to the left
            R -= 1

    return False  # No pair found

def binary_search(nums: list[int], target: int) -> int:
    L, R = 0, len(nums) - 1  # Initialize pointers

    while L <= R:  # Continue until the search space is empty
        mid = (L + R) // 2  # Calculate the middle index

        if nums[mid] == target:  # Target found
            return mid
        elif nums[mid] < target:  # Target is in the right half
            L = mid + 1
        else:  # Target is in the left half
            R = mid - 1

    return -1  # Target not found

