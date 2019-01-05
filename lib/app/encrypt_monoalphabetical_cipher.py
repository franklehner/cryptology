"""
encrypt_monoalphabetical_cipher.py
==================================

This script is the real client
"""


import attr as _attr


@_attr.s
class FileHandler(object):
    """
    Findout the filetype and open it
    """

    filename = _attr.ib()

    def specify_filetype(self):
        """
        Find out which filetype is used
        """
        return

    def get_text(self):
        """
        Return the text from file
        """
        return
