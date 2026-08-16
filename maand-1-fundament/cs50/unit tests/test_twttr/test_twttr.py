from twttr import shorten

def test_word():
    assert shorten("world") == "wrld"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_mix():
    assert shorten("HelLo") == "HlL"

def test_int():
    assert shorten("012") == "012"

def test_sign():
    assert shorten("He!lo") == "H!l"
