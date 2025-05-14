def addBinary(a : str, b : str) -> int:
    return bin(int(a, 2) + int(b, 2))[2:]

print(addBinary("110100101101011","100000101011110"))