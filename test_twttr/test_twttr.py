from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("ghtrk") == "ghtrk"

def test_shorten_only_vowels():
    assert shorten("aeiouAEIOU") == ""
def test_shorten_mixed():
    assert shorten("hello world") == "hll wrld"

def test_shorten_single_vowels():
    assert shorten("a") == ""
    assert shorten("e") == ""
    assert shorten("i") == ""
    assert shorten("o") == ""
    assert shorten("u") == ""

def test_shorten_empty():
    assert shorten("") == ""

def test_cases():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("TWiTter") == "TWTtr"
