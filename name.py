import sys

# try:
#     print("Hello, my name is", sys.argv[1] )

# except IndexError:
#     print("To few arguments")

# The above program can be written with If Else statement also
if len(sys.argv) < 2:
    print("Too few Arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, my name is", sys.argv[1])

# This can be written in other way
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
