n = int(input())

print(*[i for pair in zip(range(1, 4), range(9, 6, -1)) for i in pair])

a = input("What u thinkin fam? ")

try:
	print(int(a))
except Exception as e:
	print(f"Error: {e}")
