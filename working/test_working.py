from working import convert
import pytest

def main():
    test_time()
    test_wrong_format()
    test_wrong_hour()
    test_wrong_minute()

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5:00 PM")

def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"



def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 13 PM")

def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("7:60 AM to 8:60 PM")

if __name__ == '__main__':
    main()
