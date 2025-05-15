
def LongestEqual(words, groups):
    res = [words[0]]
    for i in range(1, len(words)):
        if groups[i] != groups[i - 1]:
            res.append(words[i])

    return res

print(LongestEqual(["e","a","b"], [0,0,1])) #output: ["e","b"] or ["a", "b"]