#pylint: disable=no-member
"""
encrypt_monoalphabetical_cipher.py
==================================

This script is the real client
"""


import attr as _attr

import lib.domain.usecases.encrypt_monoalphabetical_cipher as _encrypter
import lib.infrastructure.stream.txt.stream_txt_file as _txt_file
import lib.infrastructure.stream.pdf.stream_pdf_file as _pdf_file


@_attr.s
class Encrypter(object):
    """
    Findout the filetype and open it
    """

    filename = _attr.ib(type=[str, unicode])

    FILETYPE_MAPPING = {
        "txt": _txt_file.TextFile,
        "pdf": _pdf_file.PDFFile,
    }

    def specify_filetype(self):
        """
        Find out which filetype is used
        """
        filetype = None

        if self.filename.endswith(".txt"):
            filetype = "txt"
        elif self.filename.endswith(".pdf"):
            filetype = "pdf"
        else:
            raise TypeError("None specified file format")

        return filetype

    def get_text(self):
        """
        Return the text from file
        """
        text = self.FILETYPE_MAPPING[self.specify_filetype()](self.filename).read()

        return text

    @classmethod
    def encrypt(cls, password, sign, text):
        """
        encrypt
        """
        encrypter = _encrypter.EncryptMono(
            text=text,
            password=password,
            sign=sign
        )

        return encrypter.encrypt()

    @classmethod
    def write(cls, filename, encrypted_text):
        """
        write encrypted text
        """
        writer = _txt_file.TextFile(filename)
        writer.write(filename, encrypted_text)
