def isAcronym(words: list[str], s: str) -> bool:
    if (len(words) != len(s)):
        return False
    

    for i in range(0, len(words)):
        if(s[i] != words[i][0]):
            return False

    return True

print(isAcronym(["dvn","acafe"], "dp"))
