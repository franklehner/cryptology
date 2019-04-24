# -*- coding: utf-8 -*-
"""
Test for decryption of a monoalphabetical encrypted text
"""


import string as _string
import pytest as _pytest
import lib.domain.usecases.decrypt_monoalphabetical_cipher as _decrypter


@_pytest.mark.parametrize(
    "password,sign,expected_password", [
        ("a", "f", "a"),
        ("aa", "f", "a"),
        ("Frank", "f", "frank"),
        ("Silke", "f", "silke"),
        ("Silke+", "f", "silke"),
        ("Silke-", "f", "silke"),
        ("Si-lke--", "f", "silke"),
        ("entschen", "f", "entsch"),
    ]
)
def test_make_password_unique(password, sign, expected_password):
    """
    Test for checking and correct passwords which are not unique
    """
    text = "hallo"
    decrypter = _decrypter.Decrypter(password=password, sign=sign, text=text)
    assert expected_password == decrypter.password


def test_create_key():
    """
    Test the key
    """
    text = _string.ascii_lowercase
    password = "geheimschrift"
    sign = "e"
    decrypter = _decrypter.Decrypter(password=password, sign=sign, text=text)
    alphabet = decrypter.create_key()
    expected = "wxyzgehimscrftabdjklnopquv"
    assert alphabet == expected


@_pytest.mark.parametrize(
    "key_char,alpha_char", [
        ("w", "a"),
        ("x", "b"),
        (" ", " "),
        ("g", "e"),
    ]
)
def test_create_charmap(key_char, alpha_char):
    """
    test_create_charmap
    """
    text = _string.ascii_lowercase
    password = "geheimschrift"
    sign = "e"
    key = "wxyzgehimscrftabdjklnopquv"
    decrypter = _decrypter.Decrypter(password=password, sign=sign, text=text)
    char_map = decrypter.create_charmap(key)
    assert isinstance(char_map, dict)
    assert len(char_map) == 27
    assert char_map[key_char] == alpha_char


@_pytest.mark.parametrize(
    "text,expected", [
        ("w", "a"),
        ("x", "b"),
        ("wx", "ab"),
        ("wx ge", "ab ef"),
        ("geheimschrift", "efgfhijkglhmn"),
    ]
)
def test_decrypt(text, expected):
    """
    test decrypt
    """
    password = "geheimschrift"
    sign = "e"
    decrypter = _decrypter.Decrypter(password=password, sign=sign, text=text)
    decrypted_text = decrypter.decrypt()
    assert decrypted_text == expected
