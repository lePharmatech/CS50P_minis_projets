import sys

def main():
    # Vérification des arguments de ligne de commande
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Vérification de la validité du deuxieme argument
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file ")

    # comptages des lignes de codes

    try:
        i = 0
        with open(filename, "r") as file:
            for line in file:
                clean_line = line.lstrip()

                if clean_line == "" or clean_line.startswith("#"):
                        continue
                i += 1
        print(i)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
     main()

