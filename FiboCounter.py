import math

def fib(n: int) -> int:
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2  # Golden ratio
    psi = (1 - sqrt_5) / 2  # Conjugate of the golden ratio
    return round((phi**n - psi**n) / sqrt_5)

print(fib(8))
