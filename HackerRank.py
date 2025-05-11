def find_removal_indices(str1, str2):
    # If the length difference is not 1, return [-1]
    if len(str1) - len(str2) != 1:
        return [-1]

    indices = []
    for i in range(len(str1)):
        # Remove the character at index i and compare the resulting string with str2
        if str1[:i] + str1[i+1:] == str2:
            indices.append(i)

    # If no valid indices are found, return [-1]
    return indices if indices else [-1]

# Example usage
str1 = "abdgggda"
str2 = "abdggda"
print(find_removal_indices(str1, str2))  # Output: [3, 4, 5]