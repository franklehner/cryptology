# -*- coding: utf-8 -*-
"""
Test for encryption of a monoalphabetical text
"""


import pytest as _pytest

import lib.domain.usecases.encrypt_monoalphabetical_cipher as _emc
import lib.app.encrypt_monoalphabetical_cipher as _mono


def get_text():
    """
    Returns a text
    """
    return """Es war einmal vor langer Zeit
    eine böse Hexe.
    """


@_pytest.mark.parametrize(
    "password,sign,result", [
        ("Frank", "f", "frank"),
        ("Silke", "f", "silke"),
        ("Silke+", "f", "silke"),
        ("Silke-", "f", "silke"),
        ("Si-lke--", "f", "silke"),
        ("entschen", "f", "entsch"),
    ]
)
def test_make_password_unique(password, sign, result):
    """
    Test for uniqueness of the password
    """
    text = get_text()
    mono = _emc.EncryptMono(password, sign, text)
    password_unique = mono.make_unique()
    assert password_unique == result


def test_create_key():
    """
    Test the encryption of a text
    """
    text = "abcdefghijklmnopqrstuvwxyz"
    password = "geheimschrift"
    sign = "e"
    mono = _emc.EncryptMono(password, sign, text)
    encrypted_text = mono.create_key()
    expected = "wxyzgehimscrftabdjklnopquv"
    assert len(expected) == 26
    assert encrypted_text == expected


@_pytest.mark.parametrize(
    "alpha_char,key_char", [
        ("a", "w"),
        ("b", "x"),
        (" ", " "),
        ("e", "g")
    ]
)
def test_create_charmap(alpha_char, key_char):
    """
    test create charmap
    """
    text = get_text()
    password = "geheimschrift"
    sign = "e"
    key = "wxyzgehimscrftabdjklnopquv"
    mono = _emc.EncryptMono(password, sign, text)
    char_map = mono.create_charmap(key)
    assert isinstance(char_map, dict)
    assert len(char_map) == 27
    assert char_map[alpha_char] == key_char


@_pytest.mark.parametrize(
    "text,expected", [
        ("a", "w"),
        ("b", "x"),
        ("ab", "wx"),
        ("ab ef", "wx ge"),
        ("efgfhijkglhmn", "geheimschrift"),
        ("ö", "ag"),
        ("ü", "ng"),
        ("ß", "kk")
    ]
)
def test_encrypt(text, expected):
    """
    test enrypt
    """
    password = "geheimschrift"
    sign = "e"
    mono = _emc.EncryptMono(password, sign, text)
    encrypted_text = mono.encrypt()
    assert encrypted_text == expected

@_pytest.mark.parametrize(
    ("filename", "filetype"), [
        ("foo.txt", "txt"),
        (u"foo.txt", "txt"),
        ("foo.pdf", "pdf"),
        (u"foo.pdf", "pdf")
    ]
)
def test_specify_filetype(filename, filetype):
    """
    test file type
    """
    file_handler = _mono.FileHandler(filename)
    result_type = file_handler.specify_filetype()
    assert result_type == filetype
