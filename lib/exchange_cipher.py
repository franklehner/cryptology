# pylint: disable=invalid-name
"""
exchange_cipher.py
"""


import string as _string


class ExchangeCipher(object):
    """
    ExchangeCipher

    params:
    =======
        - text : str

    methods:
    ========
        - encrypt
        - decrypt
        - gcd
        - get_allowed_multiplicators
    """

    ALPHABET = _string.lowercase + " "

    def __init__(self, text):
        """
        Constructor
        """
        self.text = text.lower()
        self.char_map = self.__create_char_map()
        self.inverse_map = self.__create_char_map_inverse()

    def gcd(self, max_count, number):
        """
        Find the greatest common divisor
        """
        if number == 0:
            return max_count
        return self.gcd(number, max_count % number)

    def __egcd(self, number, max_count):
        """
        Extended Euclidean Algorithm
        """
        if number == 0:
            return (max_count, 0, 1)
        g, x, y = self.__egcd(max_count % number, number)
        return (g, y - (max_count / number) * x, x)

    def __mulinv(self, number, max_count):
        """
        Modular inverse
        """
        g, x, _ = self.__egcd(number, max_count)

        if g == 1:
            return x % max_count

    def __create_char_map(self):
        pass

    def __create_char_map_inverse(self):
        pass

    def encrpyt(self, mul_key, add_key):
        pass

    def decrypt(self, mul_key, add_key):
        pass
