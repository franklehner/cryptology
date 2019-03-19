"""
exif tool
"""


import datetime as _dt

import lib.domain.usecases.exif_tool as _usecase


def update_exif_date(path, old_date="2018-08-26"):
    """
    update exif date
    """
    old_date = _dt.datetime.strptime(old_date, "%Y-%m-%d")
    exif = _usecase.EXIF()
    exif_date = exif.fetch_all(path)[0]
    create_date = _dt.datetime.strptime(exif_date["CreateDate"].split()[0], "%Y:%m:%d")
    delta = exif.calculate_delta(old_date, create_date)
    exif.update_date(path, delta)
