def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    return "".join(word1) == "".join(word2)

print(arrayStringsAreEqual(["a", "bc"], ["ab", "c"]))