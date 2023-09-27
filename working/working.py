import re


def main():
    print(convert(input("Hours: ")))


def convert(time):
    match = re.match(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", time)
    if not match:
        raise ValueError("Invalid time format")

    start_hour = int(match.group(1))
    start_minute = int(match.group(2) or 0)
    start_period = match.group(3)
    end_hour = int(match.group(4))
    end_minute = int(match.group(5) or 0)
    end_period = match.group(6)

    if start_hour < 1 or start_hour > 12 or end_hour < 1 or end_hour > 12:
        raise ValueError("Invalid time format")
    if start_minute < 0 or start_minute > 59 or end_minute < 0 or end_minute > 59:
        raise ValueError("Invalid time format")
    

    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0
    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    elif end_period == "AM" and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"

if __name__ == "__main__":
    main()