# names = []
# for _ in range(3):
#     name = input("what's your name ?")
#     names.append(name)

# print(names)
# for name in sorted(names):
#     print(f"votre nom est {name}")

# E/S de fichiers

name = input("Quel est ton nom ? ")

# file = open("names.txt","a")
# # file.write(name) pour corriger le probleme de les noms se colle la
# file.write(f"{name}\n")
# file.close()

# automatiser la fermeture de fichier

# with open("names.txt", "a") as file:
#     file.write(name)

# with open("names.txt", "r") as file:
#     lines = file.readlines()
# for line in lines:
#     print(f"hello", line)   pour enlever les sauts de lignes

# with open("names.txt", "r") as file:
#     lines = file.readlines()
# for line in lines:
#     print("hello", line.rstrip())

# ameliorer tous ce code

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello", line.rstrip())

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print("ton nom est :", name)

