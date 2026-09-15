# x = int(input("Entrez le nombre: "))
# # la condition

# if x % 2 == 0:
#     print("even")
# else :
#     print("odd")

# la fonction qui gere la parité

def main():
    x = int(input("entrez la valeur: "))
    if is_even(x):
        print("even")
    else :
        print("odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

