# names = []

# for _ in range(3):
#     name = input("What's your name ? ")
#     names.append(name)

# # for iterate in a sorted list use sorted function
# for _ in sorted(names):
#     print(f"Hello, {_}")

#================================================================================#
# File I/O section :

# name = input("What's your name ?")

# """to open a file with the desired name of the file with file type extention in the first parameter,
# second parameter is for how we want to open the file like 'w','r','a' etc mode """

# file = open("names.txt","w")
# file.write(name)
# file.close()

#================================================================================#

# name = input("What's your name ?")

# """to open a file with the desired name of the file with file type extention in the first parameter,
# second parameter is for how we want to open the file like 'w','r','a' etc mode where w = write, r = read & a = append"""

# file = open("names.txt","a")
# file.write(f"{name}\n")
# file.close()


#=================================================================================#

""" with context will automatically save and close the file"""

# name = input("What's your name ?")

# with open("names.txt","a") as file:
#     file.write(f"{name}\n")

#========================================================================#

""" Read data from files  """

# with open("names.txt", "r") as file:
#     # readlines() returns a list of all lines
#     lines = file.readlines()

# for line in lines:
#     print("Hello",line.rstrip())

#===================================================================#

# Alternative way to readlines

# with open("names.txt", "r") as file:
#     for line in sorted(file):
#         print("Hello,",line.rstrip())


#=================================================================#

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}")
