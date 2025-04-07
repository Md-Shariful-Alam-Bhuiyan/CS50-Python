import random

#prompt the user for a Level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

# making random number
number = random.randint(1,level)

# Prompt for a guess and Check the number
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break

    except:
        pass
