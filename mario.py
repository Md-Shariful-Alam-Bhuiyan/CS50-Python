def main():
    print_square(4)
    print()
    print_square_2(4)


def print_square(size):
    # for each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")
        print()

# Another function for printing square
def print_square_2(size):
    for i in range(size):
        # using string multiplication
        print("#" * size)

main()
