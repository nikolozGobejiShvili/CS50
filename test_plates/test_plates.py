from plates import is_valid

def main():
    test_length()
    test_first_chars()
    test_middle()
    test_first_number()
    test_punctuation()

#test the length of the txt
def test_length():
    assert is_valid("h") == False
    assert is_valid("hello123") == False
    assert is_valid("hello") == True

#test if first two characters are letters
def test_first_chars():
    assert is_valid("12") == False
    assert is_valid("1h") == False
    assert is_valid("h1") == False
    assert is_valid(",0") == False
    assert is_valid("$he") == False
    assert is_valid("$12") == False
    assert is_valid("hel12") == True


#test if numbers are not in the middle
def test_middle():
    assert is_valid("he12l") == False
    assert is_valid("hell1") == True

#test if first number is not 0
def test_first_number():
    assert is_valid("Hel01") == False
    assert is_valid("Hel10") == True


#test if there is not any periods, spaces, or punctuation marks
def test_punctuation():
    assert is_valid("he,12") == False
    assert is_valid("h.12") == False
    assert is_valid("h;2") == False
    assert is_valid("h:,") == False
    assert is_valid("hEl12") == True

if __name__ == "__main__":
    main()