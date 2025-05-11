n = int(input().strip())
num_of_english = set(map(int, input().strip().split()))


b = int(input())
num_of_frech = set(map(int, input().strip().split()))

print(len(num_of_english.union(num_of_frech)))