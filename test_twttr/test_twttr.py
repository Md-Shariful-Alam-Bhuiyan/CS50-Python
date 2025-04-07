import sys
sys.path.append('/workspaces/32358244/twttr')

from twttr import shorten



def test_upper_lower_cases():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"
    assert shorten("TwiTter") == "TwTtr"

def test_number():
    assert shorten("12345") == "12345"
    assert shorten("0.543") == "0.543"

def test_punctuation():
    assert shorten("!@#$") == "!@#$"
