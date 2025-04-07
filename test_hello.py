from hello import hello



def test_default():
    assert hello() == "hello, world", "hello function should return hello, world"

def test_argument():
    assert hello("Anik") == "hello, Anik"

