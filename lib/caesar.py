"""
caesar.py
=========

Encrpyt or decrypt caesar cipher
"""


import string as _string


class Caesar(object):
    """
    Caesar
    ======

    parmas:
        - text encrypted or decrpyted text
    methods:
        - encrypt_caesar
        - decrypt_caesar
    """

    ALPHABET = _string.ascii_lowercase + " "

    def __init__(self, text):
        """
        Constructor
        """
        self.text = text.lower()
        self.char_map = self.__create_char_map()
        self.inverse_map = self.__create_char_map_inverse()

    def encrypt(self, key):
        """
        enrypt clear text into encrypted cipher

        parmas:
        =======
            -key: Integer to scroll chars

        returns:
        ========
            encrpyted cipher
        """
        if isinstance(key, int):
            txt = ""

            for char in self.text:
                if char not in self.ALPHABET:
                    continue

                if char == " ":
                    txt += char
                    continue

                number = (self.char_map[char] + key) % 26
                txt += self.inverse_map[number]

            return txt
        raise ValueError("Key is no Integer!: %s" % key)

    def decrypt(self, key):
        """
        decrypt with key

        parmas:
        =======
            -key : Integer for scrolling the cipher

        returns:
        ========
            clear text
        """
        if isinstance(key, int):
            txt = ""

            for char in self.text:
                if char not in self.ALPHABET:
                    continue

                if char == " ":
                    txt += char
                    continue

                number = (self.char_map[char] - key) % 26
                txt += self.inverse_map[number]

            return txt
        raise ValueError("Key is no integer!: %s" % key)

    def __create_char_map_inverse(self):
        """
        Create a char map of the alphabet
        """
        char_map = {
            i+1: self.ALPHABET[i] for i, char in enumerate(self.ALPHABET)
            if char != " "
        }
        char_map[0] = "z"
        char_map.pop(26, None)

        return char_map

    def __create_char_map(self):
        """
        Create a char map of the alphabet
        """
        char_map = {
            self.ALPHABET[i]: i+1 for i, char in enumerate(self.ALPHABET)
            if char != " "
        }
        char_map["z"] = 0
        return char_map
