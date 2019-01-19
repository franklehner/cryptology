#pylint: disable=no-member
"""
decrypt_monoalphabetical_cipher.py
==================================

This script is the real client
"""


import attr as _attr

import lib.domain.usecases.decrypt_monoalphabetical_cipher as _decrypter
import lib.infrastructure.stream.txt.stream_txt_file as _txt_file
import lib.infrastructure.stream.pdf.stream_pdf_file as _pdf_file


@_attr.s
class Decrypter(object):
    """
    Find out file type and open it
    """

    filename = _attr.ib(type=[str, unicode])

    FILETYPE_MAPPING = {
        "txt": _txt_file.TextFile,
        "pdf": _pdf_file.PDFFile,
    }

    def specify_filetype(self):
        """
        Find out which file type is used
        """
        filetype = None

        if self.filename.endswith(".txt"):
            filetype = "txt"
        elif self.filename.endswith(".pdf"):
            filetype = "pdf"
        else:
            raise TypeError("No specified file format")

        return filetype

    def get_text(self):
        """
        Return text from file
        """
        text = self.FILETYPE_MAPPING[self.specify_filetype()](self.filename).read()

        return text

    @classmethod
    def decrypt(cls, password, sign, text):
        """
        Decrypt
        """
        decrypter = _decrypter.Decrypter(
            text=text,
            password=password,
            sign=sign
        )

        return decrypter.decrypt()

    @classmethod
    def write(cls, filename, decrypted_text):
        """
        write decrypted text
        """
        writer = _txt_file.TextFile(filename)
        writer.write(filename, decrypted_text)
