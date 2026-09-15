def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("valeur de x: "))
        except ValueError:
            pass
        else:
            return x
main()
