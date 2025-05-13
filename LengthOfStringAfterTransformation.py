def lengthOfStuff(s: str, t: int) -> int:
    MOD = 10**9 + 7

    def compute_contribution(char: str, t: int) -> int:
        position = ord('z') - ord(char)

        if t <= position:
            return 1

        return pow(2, t - position, MOD)


    total_length = 0
    for char in s:
        total_length += compute_contribution(char, t)
        total_length %= MOD

    return total_length

print(lengthOfStuff("azbk", 7517))