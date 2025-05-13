def findShi(s : str) -> bool:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

        return len(set(char_count.values())) == 1

print(findShi("abacbc"))