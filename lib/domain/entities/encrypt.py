#pylint: disable=too-few-public-methods
"""
encrypt.py
==========
"""


import abc as _abc


class AbstractEncryption:
    """
    Abstract class for Encryption
    """
    __metaclass__ = _abc.ABCMeta

    @_abc.abstractmethod
    def encrypt(self):
        """
        Abstract method encrypt
        """
        raise NotImplementedError
