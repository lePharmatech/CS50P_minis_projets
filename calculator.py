x = int(input("entrez la valeur de x:"))
y = int(input("entrez la valeur de y:"))

# z = x + y ici on concatene 2 chaines de caracteres
# pour avoir des entiers on fait


print(x + y)

# les flotteurs

a = float(input("entrez la valeur de x:"))
b = float(input("entrez la valeur de y:"))
z = round(a + b)
y = a / b
print(z)
# on peut faire ca pour obtenir notre code en autre format au lien d'avoir 1000 on 1,000 :,
print(f"{z:,}")
print(f"{y:.2f}")  # arrondie à 2 chiffres apres la virgule round(a / b, 2)
