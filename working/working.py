import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    matches = re.search(r"^(([0-9][0-2]?):?([0-5][0-9])?) (AM|PM) to (([0-9][0-2]?):?([0-5][0-9])?) (AM|PM)$", s)
    if matches:
        group = matches.groups()
        if int(group[1]) > 12 and int(group[5]) > 12:
            raise ValueError
        else:
            first_section = expected_format(group[1], group[2], group[3])
            last_section = expected_format(group[5], group[6], group[7])
            final_output = f"{first_section} to {last_section}"
            return final_output

    else:
        raise ValueError


def expected_format(hour, minute, am_or_pm):
    if am_or_pm == 'AM':
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    else:
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12

    if minute == None:
        new_min = '00'
        new_time = f"{new_hour:02}" +':'+ new_min
    else:
        new_time = f"{new_hour:02}" + ':' + minute

    return new_time

if __name__ == "__main__":
    main()
