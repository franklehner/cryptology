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

    def read(self):
        """
        read text file
        """
        if not _os.path.exists(self.filename):
            raise IOError("File does not exist")

        with open(self.filename) as text_file:
            text = text_file.read()
        return text

    def write(self, filename, text):
        """
        write text file
        """
        with open(filename, "w") as file_stream:
            for line in text:
                file_stream.write(line)
