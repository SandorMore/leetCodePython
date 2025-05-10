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
    if key == "age" and value >= 18:
        print(f"Sándor can drive")
    if key == "age" and  value < 18:
        print(f"Sándor cant drive yet")


def StalinSort(*li) -> list:
    temp = []
    
    if li == sorted(li):
        print("List is already sorted!")
    else:
        for i in range(1, len(li)):
            if li[i - 1] > li[i]:
                temp.append(li[i-1])

    
    for i in temp:
        if i in list(li):
            list(li).remove(i)

    return li
    
print(StalinSort(1,2,4,3,5,7,6,11,9,10,15,11))