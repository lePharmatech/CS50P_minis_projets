# def hello(to):
#     print("hello", to.title())

# name = input("votre nom: ")
# hello(name)

# def hello(to="world"):
#     print("hello", to)

# name = input("votre nom: ")
# hello(name)
# hello();

# on peut placer la fonction en bas mais on doit faire appel a la foncton main
# def main():
#     name = input("votre nom: ")
#     hello(name)
#     hello()

# def hello(to="world"):
#     print("hello", to)

# main()

# explorons return

def main():
    x = int(input("entrez le nombre a eleve au carré "))
    print(f"le carré de {x} est :", square(x));

def square(n):
    return n * n

main()
