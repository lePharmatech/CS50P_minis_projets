# import sys
# print("my name is",sys.argv[1])

# Gestion des erreurs

import sys
# try:
#     print("my name is",sys.argv[1])
# except IndexError:
#     print("il n'y a pas d'argument")

# pour gerer efficacement l'erreur on fait

# if len(sys.argv) < 2:
#     print("Il n'y a pas d'argument")
# elif len(sys.argv) > 2:
#     print("Il y a beaucoup d'argument")
# else:
#     print("my name is",sys.argv[1])

# on peut faire sys.exit() pour analyse le probleme de maniere concret

if len(sys.argv) < 2:
    sys.exit("Il n'y a pas d'argument")
for arg in sys.argv[1:]:
    print("my name is", arg)  #  j'ai fait du slice slicing
