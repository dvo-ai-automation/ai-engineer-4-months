from plates import is_valid

def test_spatie():
    assert is_valid("CS 50") == False

def test_nummer():
    assert is_valid("123456") == False

def test_mix():
    assert is_valid("ABC123") == True

def test_zero():
    assert is_valid("AA0124") == False

def test_short():
    assert is_valid("A") == False

def test_long():
    assert is_valid("AB12345") == False

def test_digit():
    assert is_valid("AA123B") == False
