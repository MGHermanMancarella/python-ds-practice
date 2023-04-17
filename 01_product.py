def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """
    return a*b


print("product(5,2) should be 10 ", product(5,2))
print("product(0,10000) should be 0 ", product(0,10000))
