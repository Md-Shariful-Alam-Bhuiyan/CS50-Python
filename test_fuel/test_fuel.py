from fuel import convert, gauge
import pytest

# Test correct input
def test_correct_input():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('2/5') == 40 and gauge(40) == '40%'
    assert convert('0/4') == 0 and gauge(0) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'
# Test ValueError
def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/rat")

# Test ZeroDivisionError
def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
