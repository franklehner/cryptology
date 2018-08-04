#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pylint: disable=broad-except
"""
pdf_meta.py
===========
"""


import os
import argparse
from pyPdf import PdfFileReader


def get_options():
    """
    Get options from commandline
    """
    parser = argparse.ArgumentParser(description="Options for pdf_meta")
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="specify PDF file"
    )

    options = parser.parse_args()

    if not (options.path and os.path.isfile(options.path)):
        print "Usage: python scripts/pdf_meta.py -p <path>"
        exit(1)

    return parser.parse_args()


class Script(object):
    """
    Main class for this script
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
        try:
            self.print_meta()
        except Exception:
            self.options.path = self.decrpyt_pdf_file()
            self.print_meta()

    def decrpyt_pdf_file(self):
        """
        Decrypt pdf file
        """
        decr_file = "/".join(
            [
                os.path.split(self.options.path)[0],
                os.path.split(self.options.path)[-1].split(".")[0] + "_decrypted.pdf"
            ]
        )
        if os.path.exists(decr_file):
            return decr_file
        os.system("qpdf --decrypt %s %s" %(self.options.path, decr_file))
        return decr_file

    def print_meta(self):
        """
        Print out the meta data of the pdf file
        """
        pdf_file = PdfFileReader(file(self.options.path, "rb"))
        doc_info = pdf_file.getDocumentInfo()
        print "[*] PDF MetaData For: " + str(self.options.path)
        for meta_item in doc_info:
            print "[+] " + meta_item + ": " + doc_info[meta_item]


if __name__ == "__main__":
    Script().run()
