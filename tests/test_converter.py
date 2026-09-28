import pytest

from toolkit.converter import convert
from toolkit.errors import ConverterError


def test_mm_m():
    assert convert(1000, "mm", "m") == 1.0

def test_kg_g():
    assert convert(1.5, "kg", "g") == 1500.0

def test_c_f():
    assert convert(0, "c", "f") == 32.0

def test_abs_zero():
    assert abs(convert(-273.15, "c", "k")) < 1e-9

def test_unknown():
    with pytest.raises(ConverterError):
        convert(5, "xxx", "m")

def test_err():
    with pytest.raises(ConverterError):
        convert(5, "kg", "m")

def test_zero():
    with pytest.raises(ConverterError):
        convert(-300, "c", "f")

def test_uppercase():
    assert convert(1000, "MM", "M") == 1.0

def test_mixed():
    assert convert(0, "C", "F") == 32.0

def test_lower_and_upper():
    assert convert(1, "Km", "M") == 1000.0