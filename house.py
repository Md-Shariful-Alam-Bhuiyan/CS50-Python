name = input("What's your name ? ")

# Match statement similar to Switch statement like other programming language
match name:
    case "Harry" | "Hermione" | "Ron" :
        print("Gryfindoor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
