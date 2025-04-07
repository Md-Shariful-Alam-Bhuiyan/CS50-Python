import emoji

while True:
    try:
        s = input("Input: ").strip()
        if ":" in s:
            print(f"Output: {emoji.emojize(s)}")
            break
        else:
            print("Pleasse insert a valid string")

    except ValuError:
        print("Pleasse insert a valid string")
