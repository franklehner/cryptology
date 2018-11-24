"""
prime_factors.py
================
"""


def prime_factor(num):
    """
    Return prime factors
    """
    if not isinstance(num, int):
        raise TypeError("Number must be Integer.")
    res = []
    i = 2
    if num < 2:
        return []

    while num > 1:
        while num % i == 0:
            res.append(i)
            num //= i
        i += 1
    return res
