from um import count

def test_separate_um():
    assert count("um, um, um") == 3
    assert count("um?") == 1
    assert count("hello, um, World.") == 1

def test_in_word():
    assert count("Yummy") == 0
    assert count ("ummmm, interessting, um") == 1

def test_mix_letters():
    assert count("UM, um, Um") == 3
    assert count ("uM, Mu") == 1