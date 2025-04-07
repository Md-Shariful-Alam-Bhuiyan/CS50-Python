from bank import value

def test_return_zero():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value ("Hello There") == 0

def test_return_20():
    assert value("hey") == 20
    assert value("Hi") == 20
    assert value("hi there") == 20

def test_return_100():
    assert value("What's up ?") == 100
    assert value("Afternoon") == 100
    assert value("Good morning") == 100
