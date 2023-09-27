from working import convert

def test_convert_valid_format_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 PM to 3:30 PM") == "12:00 to 15:30"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_convert_valid_format_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 3 PM") == "12:00 to 15:00"
    assert convert("11 PM to 12 AM") == "23:00 to 00:00"
def test_convert_invalid_format():
    try:
        convert("9 to 5 PM")
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid time format")

    try:
        convert("13:00 PM to 2:00 PM")
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid time format")

    try:
        convert("12:60 AM to 2:00 PM")
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid time format")

    try:
        convert("9 AM  5 PM")
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid time format")
