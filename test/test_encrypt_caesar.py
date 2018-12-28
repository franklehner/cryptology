# -*- coding: utf-8 -*-
"""
test_encrypt_caesar.py
======================

Tests for Caesar encryption
"""


import pytest as _pytest

import lib.domain.usecases.caesar_chiffre as _caesar


def test_create_charmap():
    """
    create charmap
    """
    encrypter = _caesar.EncryptCaesar("hello world", 0)
    char_map = encrypter.create_char_map()
    assert char_map["a"] == 1
    assert char_map["z"] == 0
    assert max(char_map.values()) == 25
    assert min(char_map.values()) == 0
    assert not " " in char_map


def test_create_inverse_charmap():
    """
    Test the creation of an inverse char map
    """
    encrypter = _caesar.EncryptCaesar("hello world", 0)
    inverse_char_map = encrypter.create_inverse_map()
    assert inverse_char_map[1] == "a"
    assert inverse_char_map[0] == "z"
    assert max(inverse_char_map) == 25
    assert min(inverse_char_map) == 0
    assert not " " in inverse_char_map.values()


@_pytest.mark.parametrize(
    ("text", "key", "result"), [
        ("a", 0, "a"),
        ("a", 1, "b"),
        ("aa", 1, "bb"),
        ("ab", 1, "bc"),
        ("ac", 3, "df"),
        ("AC", 3, "df"),
        ("AC AA", 3, "df dd"),
        ("a", 26, "a"),
        ("a", 29, "d")
    ]
)
def test_encrypt_caesar(text, key, result):
    """
    Test the encryption of a text with caesar chiffre
    """
    encrypter = _caesar.EncryptCaesar(text, key)
    encrypted_text = encrypter.encrypt()
    assert encrypted_text == result
