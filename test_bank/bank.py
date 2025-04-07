def main():
    x = input("Greetings: ")
    x = x.strip()
    print(f'${value(x)}')


def value(greetings: str):
    x = greetings.lower()
    if x.startswith("hello"):
        return 0
    elif x.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
