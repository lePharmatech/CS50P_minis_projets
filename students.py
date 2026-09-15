import csv
# # with open("students.csv") as file:
# #     for line in file:
# #         # simplifier le code
# #         nom, maison = line.rstrip().split(',')
# #         # row = line.rstrip().split(',')
# #         #  print(f"{row[0]} est dans {row[1]}")
# #         print(f"{nom} est dans {maison}")

# students = []
# with open("students.csv") as file:
#     for line in file:
#         nom, maison = line.rstrip().split(',')
#         # print(f"{nom} est dans {maison}")
#         # students.append(f"{nom} est dans {maison}")
#         # on peut faire ca comme un dict

#         # student["name"] = nom
#         # student["house"] = maison
#         # peut etre ameliorer comme suit
#         student = {'name': nom, 'house': maison}
#         students.append(student)

# # pour trier notre programme
# def get_name(student):
#     return student['name']

# # for student in sorted(students):
# for student in sorted(students, key = get_name):
#     # print(students)
#     print(f"{student["name"]} est dans {student["house"]}")

# students = []
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({'name': row[0], 'house': row[1]})

# pour encore ameliorer le code on peut utiliser DictReader()
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({'name': row['name'], 'house': row['house'], 'eg': row['eg']})

# def get_name(student):
#     return student['name']


# for student in sorted(students, key = get_name):
#     print(f"{student["name"]} est dans {student["house"]}")


# pour ecrire dans un fichier csv
name = input("Votre nom ? ")
house = input("Votre maison ? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "house"])
    writer.writerow({"name": name, "house": house})

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} est dans {row['house']}")


