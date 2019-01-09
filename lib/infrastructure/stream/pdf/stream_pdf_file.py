"""
stream_pdf_file.pdf
===================
"""


import os as _os

from cStringIO import StringIO as _StringIO
import attr as _attr
from pdfminer.pdfinterp import PDFResourceManager as _PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter as _PDFPageInterpreter
from pdfminer.converter import TextConverter as _TextConverter
from pdfminer.layout import LAParams as _LAParams
from pdfminer.pdfpage import PDFPage as _PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed as _PDFTextExtractionNotAllowed

import lib.domain.entities.file_stream as _file_stream


@_attr.s
class PDFFile(_file_stream.AbstractFileIO):
    """
    Handle PDF files
    """

    filename = _attr.ib()

    def read(self):
        """
        read pdf file
        """
        if not _os.path.exists(self.filename):
            raise IOError("File does not exist")

        rsrcmgr = _PDFResourceManager()
        retstr = _StringIO()
        device = _TextConverter(
            rsrcmgr,
            retstr,
            codec="utf-8",
            laparams=_LAParams()
        )

        stream = file(self.filename, "rb")
        interpreter = _PDFPageInterpreter(rsrcmgr, device)

        try:
            for page in _PDFPage.get_pages(
                    stream, set(),
                    maxpages=0,
                    password="",
                    caching=True,
                    check_extractable=True):
                interpreter.process_page(page)
            text = retstr.getvalue()

            stream.close()
            device.close()
            retstr.close()
        except _PDFTextExtractionNotAllowed:
            decr_file = "/".join(
                [
                    _os.path.split(self.filename)[0],
                    _os.path.split(self.filename)[-1].split(".")[0] + "_decrypted.pdf"
                ]
            )
            if _os.path.exists(decr_file):
                text = PDFFile(decr_file).read()
            _os.system("qpdf --decrypt %s %s" % (self.filename, decr_file))
            text = PDFFile(decr_file).read()

        return text.strip()

    def write(self, filename, text):
        """
        write pdf file
        """
        with open(filename, "w") as file_stream:
            for line in text:
                file_stream.write(line)
