from numb3rs import validate


def main():
    test_format()
    test_range()

def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False
    assert validate(r"cat") == False


def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"275.255.255.255") == False
    assert validate(r"1000.255.255.255") == False
    assert validate(r"255.1000.255.255") == False
    assert validate(r"192.168.257.450") == False
    assert validate(r"192.168.198.500") == False


if __name__ == "__main__":
    main()

