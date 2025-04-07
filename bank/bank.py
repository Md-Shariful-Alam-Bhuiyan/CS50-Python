# x = input("Greetings: ")
while True:
    x = input("Greetings: ")
    try:
        x = float(x)
        print("Please Enter your greetings line correctly")
    except:
        break

x = x.strip()
x = x.lower()
if x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("$20")
else:
    print("$100")
