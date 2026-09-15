# x = int(input("What's x? "))
# print(f"x is {x}")

# try:
#     x = int(input("What's x: "))
#     print(f"x is {x}")
# except ValueError:
#     print("Entrez un entier")

# try:
#     x = int(input("what's x: "))
# except ValueError:
#     print("Vous entrez une valeur erronée")
# else:
#     print(f"x is {x}")

# je peux l'ameliorer comme suit tant que la valeur est erronée on lui demande de saisir une valeur

while True:
    try:
        x = int(input("Entrez un nombre: "))
    except ValueError:
        print("La valeur est erronée")
    else:
        break
print(f"x est {x}")

