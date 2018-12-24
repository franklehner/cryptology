"""
caesar_chiffre.py
=================
"""


import lib.domain.entities.encrypt as _encrypt


class EncryptCaesar(_encrypt.AbstractEncryption):
    """
    Encrypt caesar
    """

    def __init__(self, text, password=None):
        """
        Constructor
        """
        self.text = text
        self.password = password

    def encrypt(self):
        """
        enrypt
        """
        return

    def create_char_map(self):
        """
        char_map
        """
        return

    def create_inverse_map(self):
        """
        create inverse map
        """
        return
