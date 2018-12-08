"""
exif_tool.py
============

Read the exif files
"""


import os as _os

from lib.domain.entities.file_reader import Reader


class EXIF(Reader):
    """
    Exif class
    """
    def __init__(self, path, outfile=None):
        """
        Constructor
        """
        pass

    def read(self):
        """
        read file
        """
        pass

    def write(self):
        """
        write file
        """
        pass

    def verify_path(self):
        """
        verifies that the path exists

        Returns path exists
        """
        return

    def fetch_gps_data(self):
        """
        Fetch only gps data from file
        """
        return
