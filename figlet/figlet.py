import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

x = ['-f', '--font']

def main():
    # check command line arguments
      if len(sys.argv) == 1:
        figlet.setFont(font = random.choice(figlet.getFonts()))
        print("Output: ", figlet.renderText(input("Input: ")), sep="\n")
      elif len(sys.argv) == 3 and sys.argv[1] in x and sys.argv[2] in figlet.getFonts():
        figlet.setFont(font = sys.argv[2])
        print("Output: ", figlet.renderText(input("Input: ")), sep="\n")
      else:
        sys.exit("Error: ")
main()     