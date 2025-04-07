def main():
    while True:
        # Here au means astronomical unit
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue
    print(f'{au} is {convert(au)} m')

def convert(au):
    if not isinstance(au, (int, float)):
        raise TypeError("au must be an int or float")
    return au * 149597870700



if __name__ == '__main__':
    main()

