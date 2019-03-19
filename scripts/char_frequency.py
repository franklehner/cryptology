#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
char_frequency.py
=================
"""


from __future__ import print_function

import click as _click


@_click.command()
@_click.option("--filename", "-f", required=True, help="Specify file with text")
def cli(filename):
    """
    Get char frequency from text
    """
    pass


if __name__ == "__main__":
    cli()
