"""
encrpyt_monoalphabetical_cipher.py
==================================
"""


import re as _re
import string as _string
import collections as _collections
import lib.domain.entities.encrypt as _encrypt
import lib.domain.usecases.caesar_chiffre as _caesar


class EncryptMono(_encrypt.AbstractEncryption):
    """
    Encrypt monoalphabetical cipher

    Attributes:
        - password string
            Password for the alphabet
        - sign char
            one char for password start
    """

    def __init__(self, password, sign, text):
        """
        Constructor
        """
        if not password:
            raise TypeError("Bitte ein Passwort eingeben")

        self.password = password
        self.password = self.make_unique()
        self.sign = sign
        self.text = text

    def encrypt(self):
        """
        Encrypt method
        """
        char_map = _caesar.EncryptCaesar.create_char_map()
        char_number = char_map[self.sign]
        caesar_text = _caesar.EncryptCaesar(self.text, key=char_number)
        return caesar_text.encrypt()

    def make_unique(self):
        """
        Password has to be unique

        Returns unique password
        """
        signs = []

        for sign in self.password:
            if sign not in signs:
                signs.append(sign)

        password = "".join(signs)
        return _re.sub(r"\W", "", password.lower().replace("-", ""))

    def create_key(self):
        """
        create key
        """
        queue = _collections.deque()
        alphabet = _caesar.EncryptCaesar.ALPHABET
        alphabet = "".join(
            [char for char in alphabet.strip() if char not in self.password]
        )
        alphabet = self.password + alphabet
        for char in alphabet:
            queue.append(char)
        rotate = _string.lowercase.find(self.sign)
        queue.rotate(rotate)
        key = "".join(list(queue))
        return key
