# Read input
n, m = map(int, input().split())  # Read the size of the array and sets
array = list(map(int, input().split()))  # Read the array
A = set(map(int, input().split()))  # Read set A
B = set(map(int, input().split()))  # Read set B

# Calculate happiness
happiness = sum((1 if i in A else -1 if i in B else 0) for i in array)

# Output the result
print(happiness)