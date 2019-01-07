# -*- coding: utf-8 -*-
"""
Test for pdf file stream
"""


import pytest as _pytest

import lib.infrastructure.stream.pdf.stream_pdf_file as _pdf_file


def create_text():
    """
    create text
    """
    return "Hallo Entschen\nwie geht es dir"


def test_constructor_valid_filename():
    """
    Test the constructor
    """
    filename = "foo.pdf"

    assert _pytest.raises(
        IOError,
        "_pdf_file.PDFFile(filename='{0}').read()".format(filename)
    )


def test_read_pdf_file():
    """
    test read pdf file
    """
    expected_text = create_text()
    filename = "data/foo.pdf"
    pdf_file = _pdf_file.PDFFile(filename=filename)
    text = pdf_file.read()
    assert pdf_file.filename == filename
    assert text == expected_text
