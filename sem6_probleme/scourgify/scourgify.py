import csv
import sys

def main():
    # Verification des arguments de ligne de commande
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    filename = sys.argv[1]
    if not filename == "before.csv":
        sys.exit(f"Could not read {filename}")

    students = []

    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            house = row["house"]
            last, first = name.split(', ')
            # print(last, first, house)
            students.append({"first": first, "last": last, "house": house})
    # print(students)
    with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for student in students:
                     writer.writerow(student)
if __name__ == "__main__":
    main()
