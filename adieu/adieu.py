import inflect

p = inflect.engine()

names = []

while True:
    try:
        x = input("Name: ")
        if x != "":
            names.append(x)
        else:
            continue
    except EOFError:
        print("Adieu, adieu, to " + p.join(names))
        break
