import pytest
from src.time_format_converter import *

def test_convert_24_to_12():
    assert "11:03 pm" == convert_24_to_12("2303")

def test_convert_12_to_24():
    assert "1205 hrs" == convert_12_to_24("12:05 pm")