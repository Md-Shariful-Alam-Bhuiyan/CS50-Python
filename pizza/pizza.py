import sys
from tabulate import tabulate
import csv


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        pass

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers = "keys",tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File Doesn't exist")

if __name__ == "__main__":
    main()
