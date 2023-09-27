import sys
import csv

#main function which calls check_command_lines and encode functions
def main():
    check_command_lines()
    try:
        #defines variabe exist_file for existing file name
        exist_file = sys.argv[1]
        encode(exist_file)

    except FileNotFoundError:
        sys.exit(f"Could not read {exist_file}")

#encode function processes the information in the given file and creates new file with given name
def encode(exist_file):
    students = []
    #open file
    with open(exist_file, "r") as file:
        reader = csv.DictReader(file)
        #iterration for every row
        for row in reader:
            #split name to define first and last names
            name = row["name"].split(",")
            students.append({"first": name[1].lstrip(), "last": name[0].lstrip(), "house": row["house"]})

    #create and open new file with processed information
    with open(sys.argv[2], "w", newline= "") as file:
        writer = csv.DictWriter(file, fieldnames= ["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in students:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

#check command line arguments
def check_command_lines():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV format")
    elif ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV format")

main()