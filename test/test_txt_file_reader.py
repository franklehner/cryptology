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


def test_wrong_file_type():
    """
    Test the wrong file type
    """
    filename = "data/sample.pdf"
    assert _pytest.raises(
        TypeError,
        "_txt_file.TextFileReader(filename='{0}')".format(filename)
    )


def test_file_does_not_exist():
    """
    Test invalid filename
    """
    filename = "foo.txt"
    assert _pytest.raises(IOError, "_txt_file.TextFileReader(filename='{0}')".format(filename))
