import re

email = input("What's your email address ? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|org|)$", email, re.IGNORECASE):
    print("valid")
else:
    print("Inavalid")
