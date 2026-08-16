import pytest

from fuel import convert, gauge

def test_neg():
    with pytest.raises(ValueError):
        convert("-1/4")

def test_50():
    assert convert("1/2") == 50


def test_100():
    assert convert("4/4") == 100

def test_null():
    assert convert("0/5") == 0

def test_high():
    with pytest.raises(ValueError):
        convert("5/4")

def test_imp():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_e():
    assert gauge(0) == "E"

def test_f():
    assert gauge(100) == "F"

def test_z():
    assert gauge(60) == "60%"

def test_1():
    assert gauge(1) == "E"

def test_99():
    assert gauge(99) == "F"
