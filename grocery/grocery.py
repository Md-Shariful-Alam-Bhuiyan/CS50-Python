
items = {}
while True:
    try:
        item = input().strip().lower()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1

    except EOFError:
        for key in sorted(items.keys()):
            print(items[key], key.upper())
        break

