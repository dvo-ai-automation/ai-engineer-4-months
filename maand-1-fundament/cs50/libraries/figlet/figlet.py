from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] in ("-f", "--font"):
        if sys.argv[2] in (figlet.getFonts()):
            s = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(s))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    s = input("Input: ")
    r = random.choice(figlet.getFonts())
    figlet.setFont(font=r)
    print(figlet.renderText(s))

else:
    sys.exit("Invalid usage")
