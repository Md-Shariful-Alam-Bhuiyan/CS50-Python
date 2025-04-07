def main():
    x = input("Fraction: ").strip()
    y = convert(x)
    print(gauge(y))


def convert(fraction: str):
    while True:
        try:
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError

            if x > y:
                print("Your numerator is greater than the denominator !! Please Type Again. ")
                # fraction = input("Fraction: ").strip()
                continue

            z = (x/y)*100
            return round(z)


        except ValueError:
            print("Not an Integer. please type again..")
            # fraction = input("Fraction: ").strip()
            raise
        except ZeroDivisionError:
            print("Error: You can't divide by Zero")
            # fraction = input("Fraction: ").strip()
            raise


def gauge(percentage: int):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f'{percentage}%'

if __name__ == "__main__":
    main()

