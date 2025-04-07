coins = [25,10,5]
amount_due = 50

while amount_due > 0:
    x = int(input("Inset Coin: ").strip())
    if x in coins:
        amount_due -= x
        if amount_due > 0:
            print(f"Amount Due:{amount_due}")
        else:
            pass
    else:
        print(f"Amount Due:{amount_due}")

#calculate the changed owed
change_owed = -(amount_due)
print(f"change Owed: {change_owed}")
