from itertools import permutations

def find3Length(digits : list[int]) -> list[int]:
        res = []

        a = permutations(digits, 3)
        for i in a:
            if i[0] != 0 and i[-1] % 2 == 0:
                res.append(int("".join(map(str, i))))

        res = set(res)
        return sorted(list(res))

        

print(find3Length([1,2,3,4,0]))