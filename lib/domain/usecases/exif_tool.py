"""
exif_tool.py
============

Read the exif files
"""


import lib.domain.entities.file_stream as _file_stream


class EXIF(_file_stream.AbstractFileIO):
    """
    Exif class
    """
    def __init__(self, path, outfile=None):
        """
        Constructor
        """

    def read(self):
        """
        read file
        """

    def write(self, text):
        """
        write file
        """

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
