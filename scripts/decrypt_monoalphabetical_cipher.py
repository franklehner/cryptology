#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pylint: disable=no-value-for-parameter
"""
decrypt_monoalphabetical_cipher.py
==================================

The user gives a password and a char as Parameter from the commandline
"""


from __future__ import print_function

import click as _click
import lib.app.decrypt_monoalphabetical_cipher as _decrypter


@_click.command()
@_click.option("--password", "-p", required=True, help="Specify the password")
@_click.option("--sign", "-s", required=True, help="Specify the sign")
@_click.option("--filename", "-f", required=True, help="Specify file with text")
@_click.option("--outfile", "-o", required=True, help="Specify out file")
def cli(password, sign, filename, outfile):
    """
    decrypt monoalphabetically

    Parmas:
        - password str
        - sign char
        - file str
    """
    decrypter = _decrypter.Decrypter(filename)
    text = decrypter.get_text()
    decrypted_text = decrypter.decrypt(password, sign, text)
    decrypter.write(outfile, decrypted_text)


if __name__ == "__main__":
    cli()
