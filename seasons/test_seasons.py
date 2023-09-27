import seasons
from datetime import date



def test_calculated_minutes():
    assert seasons.days_to_minutes(1) == 1440
    assert seasons.days_to_minutes(2) == 2880
    assert seasons.days_to_minutes(10) == 14400
    assert seasons.days_to_minutes(365) == 525600

def test_reader():
    assert seasons.read_numbers(1) == "One"
    assert seasons.read_numbers(100) == "One hundred"
    assert seasons.read_numbers(2760) == "Two thousand, seven hundred sixty"
    assert seasons.read_numbers(2056700) == "Two million, fifty-six thousand, seven hundred"

def test_days_passed():
    assert seasons.days_passed("2022-04-06",  date.fromisoformat("2023-04-06")) == 365
    assert seasons.days_passed("2021-04-06",  date.fromisoformat("2023-04-06")) == 730
    assert seasons.days_passed("1997-08-13",  date.fromisoformat("2023-04-06")) == 9367
    assert seasons.days_passed("1997-08-13",  date.fromisoformat("2024-12-29")) == 10000



