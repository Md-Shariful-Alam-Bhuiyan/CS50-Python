import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip )
    if matches:
        list_of_numbers = ip.split(".")
        for num in list_of_numbers:
            if int(num) < 0 or int(num) > 255:
                return False
            else:
                pass
        return True
    else:
        return False





if __name__ == "__main__":
    main()
