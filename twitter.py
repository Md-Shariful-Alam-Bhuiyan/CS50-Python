import re

''' Extract a username from a twitter url '''


# url = input("URL : ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username : {username}")

#-----------------------------------------------------------------------------#


url = input("URL : ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
if matches:
    print(f"Username : {matches.group(1)}")
