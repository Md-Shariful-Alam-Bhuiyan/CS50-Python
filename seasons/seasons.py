from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birth_date)
        date_of_birth = date(int(year),int(month), int(day))
        difference = date.today()- date_of_birth
        total_minutes = difference.days*24*60
        new_dob = p.number_to_words(total_minutes, andword = "").capitalize()
        print(new_dob,"minutes")
    except:
        sys.exit("Invalid Date")


def check_birthday(birth_date):
    match = re.search(r"^[0-9]{4}-(0?[1-9]|1[0-2])-(0?[1-9]|1[0-9]|2[0-9]|3[0-1])$", birth_date)
    if match:
        year, month, day = birth_date.split("-")
        return year, month, day



if __name__ == "__main__":
    main()
