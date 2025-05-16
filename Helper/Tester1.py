n = int(input())
print(*range(1, n + 1), sep="")

print(*range(1,30), sep=";", end="\n", flush=True)