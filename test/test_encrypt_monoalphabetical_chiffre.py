# -*- coding: utf-8 -*-
"""
Test for encryption of a monoalphabetical text
"""


import pytest as _pytest

import lib.domain.usecases.encrypt_monoalphabetical_cipher as _emc


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
