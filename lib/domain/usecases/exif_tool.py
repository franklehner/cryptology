"""
exif_tool.py
============

Read the exif files
"""


import os as _os
import json as _json


class EXIF(object):
    """
    Exif class
    """

    def fetch_all(self, path):
        """
        read file
        """
        info = _os.popen("exiftool -j {0}".format(path))
        return _json.loads(info.read())

    def write(self, outfile):
        """
        write file
        """
        pass

    def fetch_gps_data(self):
        """
        Fetch only gps data from file
        """
        return

    def update_date(self, path, delta):
        """
        update file
        """
        _os.popen('exiftool "-AllDates-=0:0:{delta} 0:0:0" {path}'.format(delta=delta, path=path))

    def calculate_delta(self, old_date, new_date):
        """
        Calculate the delta between two timestamps
        """
        return (new_date - old_date).days
