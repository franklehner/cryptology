"""
char_frequency.py
=================
"""


import abc as _abc


class AbstractCharFrequency(object):
    """
    Abstract class for char frequency
    """
    __metaclass__ = _abc.ABCMeta

    @_abc.abstractmethod
    def get_ngrams(self, n):
        """
        Abstract method get_frequencies
        """
        raise NotImplementedError
