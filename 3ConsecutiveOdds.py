def _3ConsecutiveOdds(arr: list) -> bool:
    if len(arr) < 3:
        return False
    
    for i in range(2, len(arr)):
        if (arr[i] % 2 != 0 and arr[i - 1] % 2 != 0 and arr[i - 2] % 2 != 0):
            return True
            
    return False

print(_3ConsecutiveOdds([1,3,4,5,7]))
