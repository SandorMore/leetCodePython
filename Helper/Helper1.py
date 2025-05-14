# Convert the binary number 10101 to decimal and print it
binary_number = "10101"
decimal_number = int(binary_number, 2)
print(4 * 1.5)

import math

print(a := math.sin(30) / math.sin(40))
print(a)

print(math.sin(a)**-1)


memo = {}
def countFib(n : int) -> int:
    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return memo[n]
    memo[n] = countFib(n - 1) + countFib(n - 2)

    
print(countFib(8))

nums = [1,2,3,4]

