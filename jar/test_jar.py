from jar import Jar
import pytest

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(30)
    assert jar.capacity == 30


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(15)
    jar.deposit(2)
    assert jar.size == 2
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar = Jar(15)
        jar.deposit(16)


def test_withdraw():
    jar = Jar(15)
    jar.size = 10
    jar.withdraw(2)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar = Jar()
        jar.withdraw(7)

def test_capacity():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.capacity = -10