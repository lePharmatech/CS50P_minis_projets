import random

def main():
    # la logique du level
    while True:
        try:
            level = int(input("Level: "))
            if level < 0:
                raise ValueError
            print(level)
        except ValueError:
            pass
        else:
            break
    # affichage du nombre aleatoire
    a = random_number(level)
    # print(a)

# la logique du guess
    while True:
        try:
           guess = level = int(input("Guess: "))
           while guess <= 0:
               guess = level = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if a < guess:
                print("Too large!")
            elif a > guess:
                print("Too small!")
            else:
                print("Just right!")
                break

# la fonction qui genere le nombre aleatoire
def random_number(level):
    random_nbr = random.randint(1, level)
    return random_nbr


main()
