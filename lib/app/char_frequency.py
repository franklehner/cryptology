"""
char_frequency.py
=================
"""


import attr as _attr

import lib.domain.usecases.char_frequency as _char_frequency
import lib.infrastructure.stream.txt.stream_txt_file as _txt_file
import lib.infrastructure.stream.pdf.stream_pdf_file as _pdf_file


@_attr.s
class Frequency(object):
    """
    Get the char frequency of a file
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
