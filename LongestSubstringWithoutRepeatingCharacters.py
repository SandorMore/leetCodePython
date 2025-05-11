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
    
print(LongestSubstring("pwwkew"))


def LongestSubS(s: str) -> list:
    substrings = []
    counts = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
        
    for i in substrings:
        print(i)
        for j in range(len(i)):
            if (i.count(i[j]) <= 1):
                counts.append(len(i))

    return max(counts)
    
print(LongestSubS("abcdag"))