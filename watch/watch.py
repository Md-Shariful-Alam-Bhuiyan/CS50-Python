import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"^<iframe.*></iframe>$",s):
       if url_match := re.search(r"(https?://(www\.)?youtube\.com/embed/)([a-zA-z0-9]+)",s):
            group = url_match.groups()
            return f"https://youtu.be/{group[2]}"

    else:
        return None




if __name__ == "__main__":
    main()
