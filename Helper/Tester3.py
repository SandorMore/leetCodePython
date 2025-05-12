# Read the number of elements in set A
n = int(input().strip())
A = set(map(int, input().strip().split()))

# Read the number of other sets
N = int(input().strip())

# Perform operations on set A
for _ in range(N):
    # Read the operation name and the length of the other set
    command = input().strip().split()[0]
    # Read the elements of the other set
    s = set(map(int, input().strip().split()))
    
    # Perform the specified operation
    if command == "intersection_update":
        A.intersection_update(s)
    elif command == "update":
        A.update(s)
    elif command == "symmetric_difference_update":
        A.symmetric_difference_update(s)
    elif command == "difference_update":
        A.difference_update(s)

# Print the sum of elements in set A
print(sum(A))