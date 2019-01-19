"""
char_frequency.py
=================
"""


import attr as _attr

import lib.domain.entities.char_frequency as _char_frequency


@_attr.s
class Frequency(_char_frequency.AbstractCharFrequency):
    """
    Frequency
    """

    text = _attr.ib()

    def get_frequencies(self):
        """
        get_frequencies
        """
        pass
