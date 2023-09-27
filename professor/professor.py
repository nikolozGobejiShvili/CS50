import random

def main():
    level = get_level()
    score = all_round(level)
    print("Score:", score)

def get_level():
        while True:
            try:
                level = int(input("Level: "))
                if level > 3 or level <= 0:
                    continue
                else:
                    return level
            except:
                continue

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    if level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    if level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x, y

def round(x, y):
    count = 0
    while count < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return True
            else:
                count += 1
                print("EEE")
        except:
             count += 1
             print("EEE")
    print(f"{x} + {y} ={x + y}")
    return False

def all_round(level):
    count = 0
    score = 0
    while count < 10:
        x, y = generate_integer(level)
        answer = round(x, y)
        if answer == True:
            score += 1
        count += 1
    return score

if __name__ == "__main__":
    main()
