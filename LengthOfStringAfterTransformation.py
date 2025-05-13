def transformed_string_length(s: str, t: int) -> int:
    MOD = 10**9 + 7

    z_count = s.count('z')
    non_z_count = len(s) - z_count

    for _ in range(t):

        new_z_count = non_z_count
        non_z_count = (non_z_count + 2 * z_count) % MOD
        z_count = new_z_count

    return (non_z_count + z_count) % MOD


print(transformed_string_length("jqktcurgdvlibczdsvnsg", 7517))