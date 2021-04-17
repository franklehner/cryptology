#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
image_exifdata_fetcher.py
=========================
fetch Metadata from image and try to get their GPS-data
"""


import os as _os
import click as _click

import lib.exif_tool as _exif


def validate_path(params, ctx, value):
    if _os.path.exists(value):
        return value
    raise RuntimeError(f"Path {value} does not exist")


class Script:
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


def get_gps_data(path):
    pass


@_click.command()
@_click.option(
    "--path",
    "-p",
    type=str,
    help="specify path (file or directory",
    callback=validate_path,
)
@_click.option(
    "--outfile",
    "-o",
    type=str,
    help="outfile",
    default="data/exif_data.kml",
)
def cli(path, outfile):
    print(path)
    print(outfile)


if __name__ == "__main__":
    cli()
