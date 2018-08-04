#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
image_exifdata_fetcher.py
=========================
fetch Metadata from image and try to get their GPS-data
"""


import os
import argparse

from lib.exif_tool import EXIF
from lib.exif_tool import KML


def get_options():
    """
    Get options from commandline
    """
    parser = argparse.ArgumentParser(
        description="Options for image meta data fetcher"
    )

    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="specify path (directory or file)"
    )

    parser.add_argument(
        "-0",
        "--outfile",
        type=str,
        default="data/exif_data.kml",
        help="specify path for outfile"
    )

    options = parser.parse_args()

    if not (options.path and os.path.exists(options.path)):
        print "Usage: python script/image_exifdata_fetcher.py -p <path>"
        exit(1)

    return options


class Script(object):
    """
    Main class for this Script
    """
    def __init__(self):
        """
        Constructor
        """
        self.options = get_options()

    def run(self):
        """
        Runner method
        """
        gps = EXIF(self.options.path).fetch_gps_data()
        self.write_kml_file(gps)


    def write_kml_file(self, exif_data):
        """
        Write kml file for import in Google Earth
        """
        kml = KML(exif_data)
        kml.prepare_kml_data()
        kml.write(self.options.outfile)


if __name__ == "__main__":
    Script().run()
