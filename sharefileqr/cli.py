#!/usr/bin/env python

import click
import os.path

from sharefileqr.core import share_file


@click.command()
@click.argument("file_to_share")
@click.option(
    "--port", type=click.INT, default=4000, help="Port to run the server on."
)
@click.option(
    "--browser-display", "-b", is_flag=True,
    help="Whether to display a link for the browser of your computer in case you "
    "can't scan your terminal directly. Try with that option disabled first."
)
def cli(file_to_share: str, port: int, browser_display: bool):
    """
    Enables you to share a file with your phone using QR code scanning.
    Give this program a file, and it will display a QR code that resolves
    to a download link when scanned from your phone.
    """
    if not os.path.isfile(file_to_share):
        print(f"Provided file does not exist: {file_to_share}")

    share_file(os.path.abspath(file_to_share), port, browser_display)


if __name__ == '__main__':
    cli()
