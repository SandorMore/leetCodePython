n = int(input().strip())
num_of_english = set(map(int, input().strip().split()))


b = int(input())
num_of_frech = set(map(int, input().strip().split()))

print(len(num_of_english.symmetric_difference(num_of_frech)))
print(len(num_of_english.difference(num_of_frech)))
print(len(num_of_english.union(num_of_frech)))
print(len(num_of_english.intersection(num_of_frech)))


T = int(input().strip())
for _ in range(T):
    num_of_elements_A = int(input().strip())
    A = set(map(int, input().strip().split()))
    
    num_of_elements_B = int(input().strip())
    B = set(map(int, input().strip().split()))
    
    print(A.issubset(B))
    print(A.issuperset(B))

# Input the main set A
A = set(map(int, input().strip().split()))

# Input the number of other sets
T = int(input().strip())

# Initialize a flag to True
is_strict_superset = True

# Check each set
for _ in range(T):
    B = set(map(int, input().strip().split()))
    # Check if A is a strict superset of B
    if not (A > B):  # A > B checks for strict superset
        is_strict_superset = False
        break

# Print the result
print(is_strict_superset)