def niga(dividend, divisor):
    """
    This function takes two integers, dividend and divisor, and returns the quotient of their division.
    The function uses bit manipulation to perform the division without using the division operator.
    """
    # Handle edge cases
    if dividend == 0:
        return 0
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    
    # Determine the sign of the result
    negative = (dividend < 0) != (divisor < 0)
    
    # Work with absolute values
    dividend, divisor = abs(dividend), abs(divisor)
    
    # Initialize quotient
    quotient = 0
    
    # Perform division using bit manipulation
    for i in range(31, -1, -1):
        if (dividend >> i) >= divisor:
            dividend -= divisor << i
            quotient += 1 << i
    
    # Apply sign to the result
    result = -quotient if negative else quotient

    # Clamp to 32-bit signed integer range
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX
    return result