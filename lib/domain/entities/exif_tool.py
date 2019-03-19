"""
Abstract EXIF Tool
"""


import abc as _abc


class AbstractExifTool(object):
    """
    Base class for exif tools
    """
    __metaclass__ = _abc.ABCMeta

    @_abc.abstractmethod
    def fetch_all(self, path):
        raise NotImplementedError

    @_abc.abstractmethod
    def new_date(self, path, date):
        raise NotImplementedError

    @_abc.abstractmethod
    def write(self, outfile):
        raise NotImplementedError

    @_abc.abstractmethod
    def fetch_gps_data(self, path):
        raise NotImplementedError
