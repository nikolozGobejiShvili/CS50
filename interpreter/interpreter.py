number_to_calculate = input("write a mathematical example: ")
first_digit = float(number_to_calculate.split()[0])
second_digit = float(number_to_calculate.split()[2])

if "+" in number_to_calculate:
    print(first_digit + second_digit)
elif "-" in number_to_calculate:
    print(first_digit - second_digit)
elif "*" in number_to_calculate:
    print(first_digit * second_digit)
elif "/" in number_to_calculate:
    print(first_digit / second_digit)
else:
    print("please write correct example")