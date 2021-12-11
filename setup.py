#!/usr/bin/env python

import sys
from pathlib import Path

from setuptools import setup

assert sys.version_info >= (3, 9, 0)


def get_long_description():
    readme_md = Path(__file__).parent / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


setup(
    name="share-file-qr",
    version="0.2.0",
    packages=["sharefileqr"],
    python_requires=">=3.9",
    install_requires=["click~=8.0.3", "qrcode~=7.3.1", "tornado~=6.1"],
    entry_points={"console_scripts": ["share-file-qr=sharefileqr.cli:cli"]},
    license="GPLv3",
    description="Share files from the terminal of your computer to a smartphone by "
    "scanning a QR code.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Pierre Walch",
    author_email="contact@pwal.ch",
    url="https://github.com/pwalch/share-file-qr",
    keywords="qr code smartphone share file",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Communications :: File Sharing",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.9",
    ],
)
