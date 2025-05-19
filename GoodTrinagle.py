def tri(nums):
    if nums[0] + nums[1] <= nums[2] or nums[0] + nums[2] <= nums[1] or nums[1] + nums[2] <= nums[0]:
        return "none"
    
    for i in range(1, len(nums)):
        if nums.count(nums[i]) == 3:
            return "equilateral"

        elif nums.count(nums[i]) == 2:
            return "isosceles"

        elif nums.count(nums[i]) == 1 and nums.count(nums[i-1]) == 1:
            return "scalene"


print(tri([31, 1, 2]))