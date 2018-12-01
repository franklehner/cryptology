"""
Test for prime factors
"""
import pytest as _pytest

import lib.prime_factors as _pf


@_pytest.mark.parametrize(
    "num,res", [
        (0, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (6, [2, 3]),
        (8, [2, 2, 2]),
        (9, [3, 3]),
        (5*17*31, [5, 17, 31]),
    ]
)
def test_prime_factor(num, res):
    """
    Test the calculation of prime_factor
    """
    assert _pf.prime_factor(num) == res


@_pytest.mark.parametrize(
    "num", ["", 2.1]
)
def test_prime_factors_invalid(num):
    """
    Test the given parameter to prime_factor
    """
    assert _pytest.raises(TypeError, "_pf.prime_factor({0})".format(num))
