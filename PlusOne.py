def PlusOne(digits : list[int]) -> list[int]:
    res = []
    
    num = int(''.join(map(str, digits)))
    num += 1
    num = str(num)
    for i in num:
        res.append(int(i))
        
    return res

print(PlusOne([9]))