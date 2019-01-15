# -*- coding: utf-8 -*-
#pylint: disable=no-member
"""
decrypt_monoalphabetical_cipher.py
==================================

This program is for decrypting a monoalphabetical encrypted chiffre with a
password and a sign
"""


import re as _re
import string as _string
import collections as _collections
import pandas as _pd
import attr as _attr
import lib.domain.entities.decrypt as _decrypt


@_attr.s
class Decrypter(_decrypt.AbstractDecrypter):
    """
    Decrypt monoalphabetical cipher
    """

    password = _attr.ib()
    sign = _attr.ib()
    text = _attr.ib()

    @password.validator
    def unify_password(self, attribute, value): #pylint: disable=unused-argument
        """
        Checks if a password is given. If there is a password this method
        processes a method which makes the characters in the password unique
        if they are not.

        Params:
        =======
            - attribute
            - value
        """
        if not value:
            raise TypeError("Bitte ein Passwort eingeben")

        self.password = self.make_unique()

    @text.validator
    def validate_text(self, attribute, value): #pylint: disable=unused-argument
        """
        check text
        """
        if not isinstance(self.text, (unicode, str)):
            raise TypeError("Text is not instance of unicode or string")

    def decrypt(self):
        """
        decrypt
        """
        text_frame = _pd.DataFrame({"words": self.text.split()})
        text_frame["decrypted"] = text_frame["words"].map(self.make_decryption)

        return " ".join(list(text_frame["decrypted"]))

    def make_unique(self):
        """
        make_unique
        """
        signs = []

        for sign in self.password:
            if sign not in signs:
                signs.append(sign)

        password = "".join(signs)

        return _re.sub(r"\W", "", password.lower().replace("-", ""))

    def create_key(self):
        """
        create_key
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

    @classmethod
    def create_charmap(cls, key):
        """
        create char map
        """
        alphabet = _string.lowercase + " "
        key += " "
        char_map = {val: key for key, val in zip(alphabet, key)}

        return char_map

    def make_decryption(self, text):
        """
        make decryption
        """
        key = self.create_key()
        charmap = self.create_charmap(key)
        decrypted_text = ""

        for token in text:
            if token not in charmap:
                continue
            decrypted_text += charmap[token]

        return decrypted_text
