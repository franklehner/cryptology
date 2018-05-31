"""
Convert PDF files to text files
"""


import os as _os
from cStringIO import StringIO as _StringIO


from pdfminer.pdfinterp import PDFResourceManager as _PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter as _PDFPageInterpreter
from pdfminer.converter import TextConverter as _TextConverter
from pdfminer.layout import LAParams as _LAParams
from pdfminer.pdfpage import PDFPage as _PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed as _PDFTextExtractionNotAllowed


def convert(path):
    """
    Run converter
    """
    rsrcmgr = _PDFResourceManager()
    retstr = _StringIO()
    device = _TextConverter(
        rsrcmgr,
        retstr,
        codec="utf-8",
        laparams=_LAParams()
    )
    stream = file(path, "rb")
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
        return text
    except _PDFTextExtractionNotAllowed:
        decr_file = "/".join(
            [
                _os.path.split(path)[0],
                _os.path.split(path)[-1].split(".")[0] + "_decrypted.pdf"
            ]
        )
        if _os.path.exists(decr_file):
            return convert(decr_file)
        _os.system("qpdf --decrypt %s %s" % (path, decr_file))
        return convert(decr_file)
