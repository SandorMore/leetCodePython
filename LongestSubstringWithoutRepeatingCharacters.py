def LongestSubstring(s : str) -> int:
    counts = []
    for i in range(0, len(s)):
        count : int = 1
        f : int = 0
        for j in range(1, len(s)):
            if s[f] != s[j]:
                count += 1
                f += 1

        counts.append(count)
    
    return max(counts)
    
# print(LongestSubstring("pwwkew"))


def LongestSubS(s: str) -> int:
    counts = []
    for i in range(len(s)):
        unique_chars = set()
        count = 0
        for j in range(i, len(s)):
            if s[j] in unique_chars:
                break
            unique_chars.add(s[j])
            count += 1
        counts.append(count)

    return max(counts) if counts else 0
    
print(LongestSubS("abcdaga"))