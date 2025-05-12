from collections import Counter

K = int(input().strip())
li = list(map(int, input().strip().split()))

counts = Counter(li)
for key, value in counts.items():
    if value != K:
        print(key)
        break