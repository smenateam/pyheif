# future
from __future__ import absolute_import, unicode_literals

# stdlib
import os
import sys

# project
import pyheif

sys.path.insert(0, os.path.abspath("."))


def test_libheif_version():
    version = pyheif.libheif_version()
    assert version != ""


def test_pyheif_version():
    expected_version = "0.5.1"
    version = pyheif.__version__
    assert expected_version == version
