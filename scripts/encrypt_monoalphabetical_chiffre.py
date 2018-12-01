#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-value-for-parameter
"""
encrypt_monoalphabetical_chiffre.py
===================================

The user gives a password and a char as Parameter from the commandline
"""


from __future__ import print_function

import click as _click


@_click.command()
@_click.option("--password", "-p", required=True, help="Specify the password")
@_click.option("--sign", "-s", required=True, help="Specify the sign")
def cli(password, sign):
    """
    Encrypt monoaphetically
    Params:
        - password str
        - sign char
    """
    print(password, sign)


if __name__ == "__main__":
    cli()
