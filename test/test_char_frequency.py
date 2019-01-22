# -*- coding: utf-8 -*-
"""
Test char frequency
"""


import pytest as _pytest

import lib.domain.usecases.char_frequency as _char_frequency


@_pytest.mark.parametrize(
    "text,char,count", [
        ("a", "a", 1),
        ("aa", "a", 2),
        ("ab", "a", 1),
        ("ab", "b", 1),
    ]
)
def test_char_frequency_one(text, char, count):
    """
    Test the frequency of every char
    """
    frequency = _char_frequency.Frequency(text)
    ngrams = frequency.get_ngrams(1)
    assert ngrams[char] == count


@_pytest.mark.parametrize(
    "text,bigram,count", [
        ("ab", "ab", 1),
        ("abhaab", "ab", 2),
        ("abhaab", "bh", 1),
        ("abhaab", "ha", 1),
        ("abhaab", "aa", 1),
    ]
)
def test_char_frequency_two(text, bigram, count):
    """
    test bigrams
    """
    frequency = _char_frequency.Frequency(text)
    bigrams = frequency.get_ngrams(2)
    assert bigrams[bigram] == count


@_pytest.mark.parametrize(
    "text,trigram,count", [
        ("aaa", "aaa", 1),
        ("aaabbbb", "aaa", 1),
        ("aaabbbb", "bbb", 2),
    ]
)
def test_char_frequency_three(text,trigram,count):
    """
    test trigrams
    """
    frequency = _char_frequency.Frequency(text)
    trigrams = frequency.get_ngrams(3)
    assert trigrams[trigram] == count
