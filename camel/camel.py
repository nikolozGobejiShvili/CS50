text = input("camelCase: ")
text2 = ""

for c in text:
    if c.isupper():
        text2 += "_" + c.lower()
    else:
        text2 += c

print("snake_case: " + text2)           