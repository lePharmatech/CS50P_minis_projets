from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

def main():
    try:
        if len(sys.argv) == 1:
                    str = get_str()
                    # print(str)
                    random_font = random.choice(figlet.getFonts())
                    # print(random_font)
                    figlet.setFont(font=random_font)
                    print(figlet.renderText(str))
        elif len(sys.argv) == 3:
                    if not (sys.argv[1] in ['-f','--font'] and sys.argv[2] in figlet.getFonts()):
                          raise SystemExit
                    else:
                        #     print("ça marche")
                            str = get_str()
                            # print(str)
                            figlet.setFont(font=sys.argv[2])
                            print(figlet.renderText(str))

    except (IndexError, ValueError, SystemExit):
           sys.exit("les arguments sont incorrects")

def get_str():
      str = input("Input: ")
      return str

main()
