import pytest
from expenseV3 import valideer_input, aanvullen, totaal_optellen, maand_optellen

def test_ongeldig_bedrag():
    assert valideer_input("cat 2026-08-19, koffie") == False

def test_float():
    assert valideer_input("12.5, 2026-08-19, koffie") == {'bedrag': 12.5, 'datum': '2026-08-19', 'opmerking': 'koffie'}

def test_weinig_input():
    assert valideer_input("12.5, 2026-08-19") == False

def test_veel_input():
    assert valideer_input("12.5, 5.0, 2026-08-19, koffie") == False

def test_foute_tijd():
    assert valideer_input("12.5, 19-08-2026, koffie") == False