# -*- coding: utf-8 -*-
"""
encrpyt_monoalphabetical_cipher.py
==================================

This program is for encrypting a monoalphabetical chiffre with a password
and a sign.
"""


import re as _re
import string as _string
import collections as _collections
import pandas as _pd
import attr as _attr
import lib.domain.entities.encrypt as _encrypt


@_attr.s
class EncryptMono(_encrypt.AbstractEncryption):
    """
    Encrypt monoalphabetical cipher

    Attributes:
        - password: string
            Password for the alphabet
        - sign char: string
            one char for password start
        - text: string
            this is the text you want to encrypt
    methods:
        - unify_password
            if the user forgot to choose a password with unique characters
            this method will make it unique
        - validate_text
            validates that the text is string or unicode
        - encrypt
            encrypts the given text
        - make_unique
            unifies the character in the given password
        - create_key
            takes the regular alphabet with the password and the sign
            and creates a new alphabet which is the key for the encryption
        - create_charmap
            maps the regular alphabet with the key
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
        Check if the text is instance of string or unicode. Further special
        signs are converted in regular signs if possible

        Params:
        =======
            - attribute
            - value
        """
        special_signs = {
            "ä": "ae",
            "ö": "oe",
            "ü": "ue",
            "ß": "ss",
        }
        if not isinstance(self.text, (unicode, str)):
            raise TypeError("Text is not instance of unicode or string")
        self.text = self.text.lower()
        for key, val in special_signs.items():
            self.text = self.text.replace(key, val)

    def encrypt(self):
        """
        Encrypts the text monoalphabetical (not save)

        Returns an encrypted text
        """
        text_frame = _pd.DataFrame({"words": self.text.split()})
        text_frame["encrypted"] = text_frame["words"].map(self.make_encryption)

        return " ".join(list(text_frame["encrypted"]))

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
        Replace in the regular alphabet the character (sign) and the
        following characters with the password and start the begin of
        the regular alphabet at the end of the password. And rotates
        the alphabet. For the decryption it is important that the characters
        in the key are also unique.

        Returns the key
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
        Maps the regular alphabet with the key

        Params:
        =======
            - key: string or unicode

        Returns a dict with the mapping
        """
        alphabet = _string.lowercase + " "
        key += " "
        char_map = {key: val for key, val in zip(alphabet, key)}
        return char_map

    def make_encryption(self, text):
        """
        make_encryption
        """
        key = self.create_key()
        charmap = self.create_charmap(key)
        encrypted_text = ""

        for token in text:
            if token not in charmap:
                continue
            encrypted_text += charmap[token]

        return encrypted_text
