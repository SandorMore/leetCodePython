nums = [9,1,2,3,4,5,6,7,8,9,9]

even_nums = [num for num in nums if num % 2 == 0]

print(even_nums)
nums.pop()
print(nums)
print(nums.count(9))

a, *b, c = 1, 2, 3, 4, 5, 6, 7

print(a, b , c)

def findInfo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(findInfo(name="Sándor", age="30", city="Debrecen"))