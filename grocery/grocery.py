item_list = {}

while True:
    try:
        item= input("").upper()
        if item in item_list:
            item_list[item] += 1
        else:
            item_list[item] = 1
    except (EOFError, KeyError):
        break


for key , value in sorted(item_list.items()):
    print(value, key)