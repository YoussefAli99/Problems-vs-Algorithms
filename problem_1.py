def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
        number(int): Number to find the floored squared root
    Returns:
        int: Floored Square Root
    """

    if number**2 == number:
        return number
    low, high = 0, number
    while low <= high:
        m = (low + high) // 2
        if (m**2 == number) or (m**2 <= number and (m+1)**2 > number):
            return m
        elif (m**2 > number):
            high = m
        else:
            low = m

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
