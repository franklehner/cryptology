"""
caesar_chiffre.py
=================
"""


import string as _string

import lib.domain.entities.encrypt as _encrypt


class EncryptCaesar(_encrypt.AbstractEncryption):
    """
    Encrypt caesar
    """

    ALPHABET = _string.ascii_lowercase + " "

    def __init__(self, text, key=0):
        """
        Constructor
        """
        self.text = text.lower()
        self.key = key

    def encrypt(self):
        """
        enrypt
        """
        encrypted_text = ""

        for char in self.text:
            if char not in self.ALPHABET:
                continue

            if char == " ":
                encrypted_text += char
                continue

            char_map = self.create_char_map()
            inverse_map = self.create_inverse_map()

            number = (char_map[char] + self.key) % 26
            encrypted_text += inverse_map[number]

        return encrypted_text

    @classmethod
    def create_char_map(cls):
        """
        char_map
        """
        alphabet = _string.ascii_lowercase + " "
        char_map = {
            key: i+1 for i, key in enumerate(alphabet) if key != " "
        }
        char_map["z"] = 0
        return char_map

    @classmethod
    def create_inverse_map(cls):
        """
        create inverse map
        """
        alphabet = _string.ascii_lowercase + " "
        inverse_char_map = {
            i+1: char for i, char in enumerate(alphabet) if char != " "
        }
        inverse_char_map[0] = "z"
        inverse_char_map.pop(26, None)
        return inverse_char_map
