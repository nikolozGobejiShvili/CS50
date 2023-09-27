import sys, csv
from tabulate import tabulate


def pizza(argument):
    list=[]


    if len(argument) < 2:
        sys.exit("too few  commnad-line argument")
    if len(argument) > 2:
        sys.exit("too many command-line argument")
    if argument[1].split(".")[1] != "csv":
        sys.exit("not a csv file")
    # if argument[1] != ["sicilian.csv", "regular.csv"]:
    #     sys.exit("isn't correct format")
    try:
        with open( argument[1] , newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                list.append(row)
        headres = list[0]
        table =list[1:]
        print(tabulate(table, headres, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    pizza(sys.argv)