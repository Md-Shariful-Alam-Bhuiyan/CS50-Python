import pytest
from convert import convert

def test_int_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000

# Test for raising certain errors, exceptions and so on
def test_error():
    with pytest.raises(TypeError):
        convert("1")

def test_float_conversion():
    # pytest.approx() used for approximation of what we could expect for floating point values
    # and "abs" is the tollerance level we can accept for both slightly positive or negative changes
    # Here 1e-5 means 1*10^-5
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)
