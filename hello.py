name = input("what's your name: ")

# supprimer l'espace de part et d'autre de la saisie de l'utilisateur on a strip
name = name.strip();
# mettre en majuscule la premiere lettre qui commenceun mot
name = name.title();

# on peut faire name = name.strip().title() pour faciliter les choses
# faire aussi name = input("what's your name: ").strip().title()

print("hello, world", name,end = ""); # si on fait end = ""; il n'y a pas de saut de ligne.
print(" pas de saut de ligne")

# on peut faire
print(f"hello, {name}")

