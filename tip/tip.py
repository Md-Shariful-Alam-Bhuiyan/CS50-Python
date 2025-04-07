def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d:str):
    x = d.removeprefix("$")
    x = float(x)
    return float((f"{x:.1f}"))



def percent_to_float(p:str):
    x = p.removesuffix("%")
    x = float(x)
    decimal_value = x/100
    return decimal_value


main()
