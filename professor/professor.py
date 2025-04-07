import random

def main():
    level = get_level()
    result = simulate_game(level)
    print(f"Score: {result}")


def get_level():
    while True:
        # Get the level and check if it is between 1 and 3
        try:
            level = int(input("Level: "))
            if (level == 1 or level == 2 or level == 3 ):
                break
            else:
                pass
        except:
            pass
    return level

# Generate random Integer according to the level
def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y= random.randint(100,999)
    return x,y

# Simulate each Round for the Gane
def simulate_round(x,y):
    counter = 1
    while counter <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x+y):
                return True
            else:
                counter += 1
                print("EEE")

        except:
            counter += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

# Simulate the game
def simulate_game(level):
    counter = 1
    score = 0
    while counter <= 10:
        x,y = generate_integer(level)
        response = simulate_round(x,y)
        if response == True:
            score += 1
        counter += 1
    return score


if __name__ == "__main__":
    main()
