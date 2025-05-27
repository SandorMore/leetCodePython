n = int(input())

print(*[i for pair in zip(range(1, 4), range(9, 6, -1)) for i in pair])

a = input("What u thinkin fam? ")

try:
	print(int(a))
except Exception as e:
	print(f"Error: {e}")

nums = [1,2,3,4,5,6,7]
for i in range(0, len(nums)):
	print(i)
try:
	print(bin(64))
except Exception as es:
	print(f"Error as: ")

print()

print("Learning vim notation in vsc")