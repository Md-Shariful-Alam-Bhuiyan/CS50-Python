import random

cards = ["jack", "king", "queen"]

def main():
    # # pseudorandom number generator . use random.seed(any number) for debugging any certain outcome.
    # random.seed(9)

    # for random selection from a choice list
    # print(random.choice(cards))

    ''' for random multiple selection from a choice list with sampling replacement. it is also possible to choose
     more intentional selection with the "weights" parameter within a range of 100% in totall distribution.
     Here "k" is the number of item we want to select from a list randomly '''

    print(random.choices(cards, weights =[70,20,10],  k=2))

    # for random multiple selection from a choice list without sampling replacement
    # print(random.sample(cards, k=2))



if __name__ == "__main__":
    main()
