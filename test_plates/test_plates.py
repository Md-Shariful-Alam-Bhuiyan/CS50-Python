from plates import is_valid

# plates may contain a maximum of six characters and a minimum of 2 characters
def test_min_and_max_character():
    assert is_valid("AB") == True
    assert is_valid("ABCD12") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEF2") == False

# plates must starts with at least two letters
def test_starts_with_two_letters():
    assert is_valid("AB") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("55") == False

# numbers cannot be used in the middle of the plate; they must come at the end
def test_numbers_position():
    assert is_valid("ASD2") == True
    assert is_valid("AS2D") == False

# The first number used cannot be a '0'
def test_first_number():
    assert is_valid("AD51") == True
    assert is_valid("ASD012") == False

# No periods, spaces, or punctuation marks are allowed.
def test_punctuation():
    assert is_valid("AS1.34") == False
    assert is_valid("As1!24") == False
    assert is_valid("AS 245") == False
    assert is_valid("As*123") == False
