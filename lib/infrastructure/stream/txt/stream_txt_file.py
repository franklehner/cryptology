"""
stream_txt_file.py
==================

read and write textfile
"""


import os as _os
import attr as _attr

import lib.domain.entities.file_stream as _file_stream


@_attr.s
class TextFile(_file_stream.AbstractFileIO):
    """
    Open text files
    """
    filename = _attr.ib()
    @filename.validator
    def validate_filename(self, attribute, value): #pylint: disable=unused-argument
        """
        validate filename
        """
        if value == self.filename:
            pass

        if not value.endswith(".txt"):
            raise TypeError("Please use txt file")

    def read(self):
        """
        read text file
        """
        if not _os.path.exists(self.filename):
            raise IOError("File does not exist")

        with open(self.filename) as text_file:
            text = text_file.read()
        return text

    def write(self, text):
        """
        write text file
        """
        with open(self.filename, "w") as file_stream:
            for line in text:
                file_stream.write(line)
