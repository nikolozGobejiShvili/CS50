import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ipv4 = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    if re.search(ipv4, ip):
        return True
    return False

if __name__ == "__main__":
    main()