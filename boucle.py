# i = 0
# while i < 3:
#     print("meow")
#     i += 1

# for  i in [0, 1, 2]:
#     print("meow")

# for i in range(5):
#     print("meow")

# for _ in range(5):
#     print("meow")

# print("oui" * 3);
# print("oui \n" * 3, end="")

# while True:
#     n = int(input("Entrez le nombre superieur à 1: "))
#     if n < 0:
#         continue
#     else:
#         break

# while True:
#     n = int(input("Entrez le nombre superieur à 1: "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

def main():
    meow(get_number())


def get_number():
    while True:
        n = int(input("entre le nombre: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()






