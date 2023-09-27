from numb3rs import validate

def test_valid_ipv4():
    assert validate("192.168.0.1") == True
    assert validate("10.0.0.0") == True
    assert validate("172.16.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid_ipv4():
    assert validate("256.0.0.0") == False
    assert validate("0.256.0.0") == False
    assert validate("0.0.299.0") == False
    assert validate("0.0.0.256") == False
    assert validate("0.15,5.0.255") == False
    assert validate("cat") == False
    assert validate("...") == False