import csv
import sys
from tabulate import tabulate

def main():
    # verification des arguments de lignes de codes
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    table = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                # print(f"{row[0]}, {row[1]}, {row[2]}")
                table.append([row[0], row[1], row[2]])
        # print(table)
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()
