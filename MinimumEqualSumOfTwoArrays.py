def minSum(nums1 = [], nums2 = []) -> int:
    numOfZeros1 : int = nums1.count(0)
    numOfZeros2 : int = nums2.count(0)

    sumOfNums1 : int = sum(nums1) + (numOfZeros1)
    sumOfNums2 : int = sum(nums2) + (numOfZeros2)
    
    if (numOfZeros1 == 0 and nums2 > nums1) or (numOfZeros2 == 0 and nums1 > nums2):
        return -1
    
    return max(nums1, nums2)

print(minSum([0,1,2,3,4,5,0,1,0], [1,2,0,4,0,5,0,1]))