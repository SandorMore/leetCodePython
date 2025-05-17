def longestPalindrome(s: str) -> str:
    if not s or len(s) == 1:
        return s

    start, end = 0, 0

    for i in range(len(s)):
        # Odd length palindrome
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l > end - start:
                start, end = l, r
            l -= 1
            r += 1
        # Even length palindrome
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l > end - start:
                start, end = l, r
            l -= 1
            r += 1

    return s[start:end+1]