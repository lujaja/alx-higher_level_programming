#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>


def add_integer(a, b=98):
    """Computes and returns sum of 2 integers.

    Args:
        a (int/float): First operant in addintion.
        b (int/float): second operant in addition.
    Returns:
        int: result of arithmetix operation of 'a' and 'b' are
        casted to integer before addition if there was a float
        in the operants.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
