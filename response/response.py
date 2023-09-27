from validators import email

def main():
    print(validate_email(input("What's your email adress? ")))

def validate_email(e):
    if email(e):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()