"""
stream_txt_file.py
==================

read and write textfile
"""


import os as _os
import attr as _attr

import lib.domain.entities.file_reader as _file_reader


@_attr.s
class TextFileReader(_file_reader.AbstractReader):
    """
    Open text files
    """
    filename = _attr.ib()
    @filename.validator
    def validate_filename(self, attribute, value): #pylint: disable=unused-argument
        """
        validate filename
        """
        if not value.endswith(".txt"):
            raise TypeError("Please use txt file")

        if not _os.path.exists(self.filename):
            raise IOError("File does not exist")

    def read(self):
        """
        read text file
        """
        with open(self.filename) as text_file:
            text = text_file.read()
        return text

    def write(self):
        """
        write text file
        """
        pass
