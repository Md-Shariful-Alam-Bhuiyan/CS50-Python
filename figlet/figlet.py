import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

# Checking whether system cli argument is only one
if len(sys.argv) == 1:
    isRandomFont = True
    name = input("Input: ")
    figlet.setFont(font=random.choice(fonts))

# Checking whether system cli argument is only three
elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        isRandomFont = False
        name = input("Input: ")
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

try:
    if isRandomFont == True:
        print(f"Output:\n{figlet.renderText(name)}")
    elif isRandomFont == False:
        print(f"Output:\n {figlet.renderText(name)}")

except:
    sys.exit("Invalid usage")
