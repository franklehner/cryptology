#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Manipulating exif data
"""


import os as _os
import click as _click

import lib.app.exif_tool as _app


@_click.command()
@_click.option("--filename", "-f", required=True)
@_click.option("--outfile", "-o", required=True)
@_click.option("--target-timestamp", "-t", required=True)
def cli(filename, outfile, target_timestamp):
    """
    Client
    """
    #_app.update_exif_date(filename, target_timestamp)
    if _os.path.isfile(filename):
        _app.update_exif_date(filename, target_timestamp)
        print(filename)
    else:
        if _os.path.exists(filename):
            files = [file for file in _os.listdir(filename) if file.endswith(".jpg")]
            for file in files:
                target = _os.path.join(filename, file)
                _app.update_exif_date(target, target_date)
        else:
            raise IOError("Invalid file path")


if __name__ == "__main__":
    cli()
