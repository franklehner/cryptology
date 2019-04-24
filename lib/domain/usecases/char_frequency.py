"""
char_frequency.py
=================
"""


import attr as _attr
import collections as _collections

import lib.domain.entities.char_frequency as _char_frequency


@_attr.s
class Frequency(_char_frequency.AbstractCharFrequency):
    """
    Frequency
    """

    text = _attr.ib()

    def get_ngrams(self, n):
        """
        get_ngrams
        """
        ngrams = _collections.defaultdict(int)

        for i, _ in enumerate(self.text):
            ngrams[self.text[i:i+n]] += 1

        ngrams = {key: val for key, val in ngrams.items() if len(key) == n}

        return ngrams
