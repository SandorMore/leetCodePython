def ClimbStairs(n):
    one, two = 1, 1

    for i in range(n - 1):
        one, two = two, one + two

    return two

print(ClimbStairs(12))