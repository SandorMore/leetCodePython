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

dict = {
    "name": str("Sándor"),
    "age": int(17),
    "occupation": bool(False),
}

for key, value in dict.items():
    if key is "age" and value >= 18:
        print(f"Sándor can drive")
    if key is "age" and  value < 18:
        print(f"Sándor cant drive yet")


def StalinSort(*li) -> list:
    temp = []
    for i in range(1, len(li)):
        if li[i] > li[i + 1]:
            temp.append(i)

    return li - temp
        
print(StalinSort(1,2,4,3,5,7,6,11,9,10,15,11))