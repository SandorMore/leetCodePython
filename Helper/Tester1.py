n = int(input())
print(*range(3) *range(0,3,1) *range(10, 7 - 1, -1), sep="")

print(*[i for pair in zip(range(1, 4), range(9, 6, -1)) for i in pair])