"""
exif_tool.py
============

This tool fetches the exif data from images or pdf-files
"""


import os as _os
import json as _json


class EXIF:
    """
    Fetch exif data with linux exiftool

    Attributes:
        - path: Complete path with filename

    Methods:
        - fetch_all_exif_data
        - fetch_gps_data
        - verify_path
        - calulate_gps
    """
    def __init__(self, path):
        """
        Constructor

        Params:
            - path: Complete path with filename
        """
        self.path = path

    def __verify_path(self):
        """
        Verifies that the path exists

        Returns path exists
        """
        return _os.path.exists(self.path)

    def fetch_all_exif_data(self):
        """
        Fetch all exif data and give it to json
        """
        if not self.__verify_path():
            raise RuntimeError("Path does not exist!")
        info = _os.popen(f"exiftool -j {self.path}")
        return _json.loads(info.read())

    def fetch_gps_data(self):
        """
        Fetch only gps data from file
        """
        if not self.__verify_path():
            raise RuntimeError("Path does not exist!")
        info = _os.popen(
            f"exiftool -gpslatitude -gpslongitude -j -n {self.path}",
        )
        return _json.loads(info.read())

    @staticmethod
    def calculate_gps(deg=None, minute=None, sec=None):
        """
        Convert GPS date to decimal
        """
        if not (deg and minute and sec):
            raise RuntimeError("please insert degree, minute and second")
        return (sec/60 + minute) / 60 + deg


def fetch_gps_data(path):
    """fetch the gps data
    """
    gps_data = _os.popen(
        f"exiftool -gpslatitude -gpslongitude -j -n {path}",
    )

    return _json.loads(gps_data.read())


class KML:
    """
    Class KML
    """
    def __init__(self, gps_data):
        """
        Constructor
        """
        self.gps_data = gps_data
        self.names = []
        self.longitudes = []
        self.latitudes = []

    def prepare_kml_data(self):
        """
        Prepare the date for writing
        """
        for gps in self.gps_data:
            if "GPSLongitude" not in gps or "GPSLatitude" not in gps:
                continue
            self.names.append(gps.get("SourceFile"))
            self.longitudes.append(gps.get("GPSLongitude"))
            self.latitudes.append(gps.get("GPSLatitude"))

    def write(self, filename="data/exif_data.kml"):
        """
        Write kml file
        """
        with open(filename, "w", encoding="utf-8") as f_name:
            f_name.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            f_name.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">")
            f_name.write("<Document>\n")
            for name, longi, lati in zip(self.names, self.longitudes, self.latitudes):
                f_name.write("<Placemark>\n")
                f_name.write(f"<name>{name}</name>\n")
                f_name.write("<Point>\n")
                f_name.write(f"<coordinates>{longi},{lati}</coordinates>\n")
                f_name.write("</Point>\n")
                f_name.write("</Placemark>\n")
            f_name.write("</Document>\n")
            f_name.write("</kml>\n")
