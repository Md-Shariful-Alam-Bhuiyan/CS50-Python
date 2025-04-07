while True:
    try:
        x = int(input("What is x ?"))
    except ValueError:
        print("X is not an integer")
    else:
        break
print(f"x is {x}")
