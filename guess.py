def get_guess():
    guess = int(input("Enter your guess :"))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("Correct")
    else:
        print("Incorrect")

main()
