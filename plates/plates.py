#main function calls is_valid function to check plate
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#is_valid function
def is_valid(txt):
    #main loop
    while True:
        #check the length of the txt
        if len(txt) < 2 or len(txt) > 6:
            return False

        #check if first two characters are letters
        for l in txt[:2]:
            if not l.isalpha():
                return False

        #check if numbers are not in the middle
        for n in txt:
            if n.isdigit():
                index = txt.index(n)
                if not txt[index:].isdigit():
                    return False

        #check if first number is not 0
        i = 0
        while i < len(txt):
            if txt[i].isdigit() == True:
                if txt[i] == "0":
                    return False
                break
            i += 1

        #check if there is not any periods, spaces, or punctuation marks
        for s in txt:
            if s in [".", ",", "!", "?", " ", "\"", "\'"]:
                return False

        return True

#call main function
main()