# -*- coding: utf-8 -*-
"""
Test for text file reader
"""


import pytest as _pytest

import lib.infrastructure.stream.txt.stream_txt_file as _txt_file


def test_constructor_valid_filename():
    """
    Test the constructor
    """
    filename = "data/1026778984.txt"
    text_reader = _txt_file.TextFileReader(filename)
    assert filename == text_reader.filename


@_pytest.mark.parametrize(
    "filename", [
        "data/1026778984.pdf",
        "data/1026778984.gz"
    ]
)
def test_wrong_file_type(filename):
    """
    Test the wrong file type
    """
    assert _pytest.raises(
        TypeError,
        "_txt_file.TextFileReader(filename='{0}')".format(filename)
    )


def test_file_does_not_exist():
    """
    Test invalid filename
    """
    filename = "foo.txt"
    assert _pytest.raises(
        IOError,
        "_txt_file.TextFileReader(filename='{0}')".format(filename)
    )


def test_read_text():
    """
    test read text
    """
    filename = "data/1026778984.txt"
    text_reader = _txt_file.TextFileReader(filename=filename)
    text = text_reader.read()
    assert text
    assert isinstance(text, (str, unicode))
    assert len(text) == 393566
