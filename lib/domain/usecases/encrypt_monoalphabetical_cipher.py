"""
encrpyt_monoalphabetical_cipher.py
==================================
"""


import re as _re
import string as _string
import collections as _collections
import attr as _attr
import lib.domain.entities.encrypt as _encrypt


@_attr.s
class EncryptMono(_encrypt.AbstractEncryption):
    """
    Encrypt monoalphabetical cipher

    Attributes:
        - password string
            Password for the alphabet
        - sign char
            one char for password start
    """

    password = _attr.ib()
    sign = _attr.ib()
    text = _attr.ib()
    @password.validator
    def unify_password(self, attribute, value): #pylint: disable=unused-argument
        """
        unify password
        """
        if not value:
            raise TypeError("Bitte ein Passwort eingeben")
        self.password = self.make_unique()

    def encrypt(self):
        """
        Encrypt method
        """
        return

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
        alphabet = _string.lowercase
        alphabet = "".join(
            [char for char in alphabet if char not in self.password]
        )
        alphabet = self.password + alphabet
        for char in alphabet:
            queue.append(char)
        rotate = _string.lowercase.find(self.sign)
        queue.rotate(rotate)
        key = "".join(list(queue))
        return key
