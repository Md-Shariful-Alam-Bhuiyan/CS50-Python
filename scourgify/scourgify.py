import csv
import sys

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith('.csv') or  not sys.argv[2].endswith('.csv'):
        sys.exit("Either one or both of the given file is not a CSV file")
    else:
        pass

    try:
        with open(sys.argv[1]) as file , open(sys.argv[2], "w") as after:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(after, fieldnames=["first","last","house"])
            writer.writeheader()

            for row in reader:
                full_name = row['name'].split(",")
                first_name = full_name[1].strip()
                last_name = full_name[0].strip()
                house = row['house']
                writer.writerow({
                    "first" : first_name,
                    "last" : last_name,
                    "house" : house
                })

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")



if __name__ == "__main__":
    main()
