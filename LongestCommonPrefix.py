def longestCommonPrefix(strs) -> str:
    if not strs:
        return ""
    
    prefix = []
    for i in range(len(strs[0])):
        char = strs[0][i]
        if all(len(s) > i and s[i] == char for s in strs):
            prefix.append(char)
        else:
            break

    return "".join(prefix)

longestCommonPrefix(["flower", "flow", "flight"])