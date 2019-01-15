"""
decrypt.py
==========
"""


import abc as _abc


class AbstractDecryption(object):
    """
    Abstract class for decryption
    """
    __metaclass__ = _abc.ABCMeta

    @_abc.abstractmethod
    def decrypt(self):
        """
        Abstract method decrypt
        """
        raise NotImplementedError
