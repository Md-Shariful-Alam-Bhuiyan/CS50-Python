import re

# name = input("whats your name ? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last,first = matches.groups()
#     name = f"{first} {last}"

# print(f"Hello, {name}")


#-------------------------------------------------#

# name = input("whats your name ? ").strip()

# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last= matches.group(1)
#     first = matches.group(2)
#     name = f"{first} {last}"

# print(f"Hello, {name}")


#-----------------------------------------------------#

# name = input("whats your name ? ").strip()

# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)

# print(f"Hello, {name}")


#-------------------with walrus operator---------------#

name = input("whats your name ? ").strip()

# Assigning to a variable and ask a boolean question simultaneously
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")
