items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

item_chosen = []


def calculate_total(order: list):
    price = 0
    for item in order:
        if item in items:
            price += items[item]
        # else:
        #     raise KeyError
    print("None", end="")
    print(f"\nTotal: ${price:.2f}")

def main():
    while True:
        try:
            name = input("Item: ").strip().title()
            if name not in items:
                continue
            item_chosen.append(name)
        # #     except KeyError:
        # #         print("Item is not found in the set of existing menu")
        # # print("\n")

        except EOFError:
            calculate_total(item_chosen)
            break


main()


