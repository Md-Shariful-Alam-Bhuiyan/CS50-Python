def main():
        name = input("camelCase : ")
        y = snake_case(name)
        print("snake_case :", y)

# Convert camelCase to snakecase
def snake_case(string):
    for i in string:
        if i.isupper():
            string = string.replace(i,"_"+i.lower())
        else:
            pass
    return string

main()
