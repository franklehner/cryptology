"""
file_reader.py
==============

Read file
"""


import abc as _abc


class AbstractFileIO(object):
    """
    Base class for file reader
    """
    __metaclass__ = _abc.ABCMeta

    @_abc.abstractmethod
    def read(self):
        """
        read method
        """

    @_abc.abstractmethod
    def write(self, text):
        """
        write method
        """
