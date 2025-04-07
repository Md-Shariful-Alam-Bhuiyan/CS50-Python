user =  input("Expression: ")
user = user.strip()

x,y,z = user.split(" ")
x = int(x)
z = int(z)

if y == "+":
    l = float(x+z)
    print(f"{l:.1f}")
elif y == "-":
    m = float(x-z)
    print(f"{m:.1f}")
elif y == "*":
    n = float(x * z)
    print(f"{n:.1f}")
else:
    o = float(x/z)
    print(f"{o:.1f}")
