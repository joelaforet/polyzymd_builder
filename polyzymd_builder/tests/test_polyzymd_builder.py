"""
Unit and regression test for the polyzymd_builder package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import polyzymd_builder


def test_polyzymd_builder_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "polyzymd_builder" in sys.modules
