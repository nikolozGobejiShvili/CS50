import re

def main():
    print(count(input("Text: ")))

def count(text):
    text = text.lower().strip()
    um = r'\bum\b'
    matches = re.findall(um, text)
    return len(matches)

if __name__ == "__main__":
    main()