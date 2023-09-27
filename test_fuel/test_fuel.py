from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_ZeroDivision()
    test_ValueError()

#test only convert function
def test_convert():
    assert convert("1/2") == 50
    assert convert("99/99") == 100
    assert convert("1/100") == 1

#test only gauge function
def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

#test ZeroDivisionError
def test_ZeroDivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

#test ValueError
def test_ValueError():
    with pytest.raises(ValueError):
        convert("cat/dog")


if __name__ == "__main__":
    main()