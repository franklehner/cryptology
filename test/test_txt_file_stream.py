# -*- coding: utf-8 -*-
"""
Test for text file reader
"""


import os as _os
import pytest as _pytest
import six as _six

import lib.infrastructure.stream.txt.stream_txt_file as _txt_file


def create_text(multiline=False):
    """
    create a sample text
    """
    if not multiline:
        text = "Hallo Entschen"
    else:
        text = "Hallo Entschen\nwie geht es dir"

    return text


def test_constructor_valid_filename():
    """
    Test the constructor
    """
    filename = "data/1026778984.txt"
    text_file = _txt_file.TextFile(filename)
    assert filename == text_file.filename


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
        "_txt_file.TextFile(filename='{0}')".format(filename)
    )


def test_file_does_not_exist():
    """
    Test invalid filename
    """
    filename = "foo.txt"
    assert _pytest.raises(
        IOError,
        "_txt_file.TextFile(filename='{0}').read()".format(filename)
    )


def test_read_text():
    """
    test read text
    """
    filename = "data/1026778984.txt"
    text_file = _txt_file.TextFile(filename=filename)
    text = text_file.read()
    assert text
    assert isinstance(text, _six.string_types)

@_pytest.mark.parametrize(
    "multiline", [
        False,
        True
    ]
)
def test_write_file(multiline):
    """
    test writing file
    """
    filename = "/tmp/foo.txt"
    text = create_text(multiline)
    text_file = _txt_file.TextFile(filename)
    text_file.write(text)
    assert _os.path.exists(filename)
    with open(filename) as file_stream:
        text_stream = file_stream.read().strip()

    assert text_stream == text
