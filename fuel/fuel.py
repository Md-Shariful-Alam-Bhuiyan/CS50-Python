
def main():
    fuel_gauge()

def fuel_gauge():
    while True:
        try:
            x = input("Fraction: ").strip()
            x,y = x.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError

            if x > y:
                print("Your numerator is greater than the denominator !! Please Type Again. ")
                continue
            z = (x/y)*100
            if z <= 1:
                 return print("E")
            elif z >= 99:
                return print("F")
            else:
                return print(f"{round(z)}%")

        except ValueError:
                print("Not an Integer. please type again..")
        except ZeroDivisionError:
                print("Error: You can't divide by Zero")


if __name__ == "__main__":
    main()
