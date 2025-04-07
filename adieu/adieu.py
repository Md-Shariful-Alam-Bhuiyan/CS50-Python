import sys


names = []
tag = "Adieu, adieu, to "
# taking Input untill user press ctrl+D
try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    if len(names) == 0:
        print("There is no input")
    if len(names) == 1:
        print("\n"+tag + names[0])
    elif len(names) == 2:
        print("\n"+tag + names[0] + " and "+ names[1])
    elif len(names) >= 3:
        print("\n"+tag + names[0] + ", "+ names[1], end = ", ")
        for item in range(2,len(names)-1):
            print(names[item]+",", end =" ")
        print("and "+names[-1])
    else:
        sys.exit("Try Again")


