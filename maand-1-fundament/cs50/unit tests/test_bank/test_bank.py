from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("h") == 20

def test_empty():
    assert value("") == 100

def test_long():
    assert value("Hello there") == 0

def test_upper():
    assert value("Hello") == 0
