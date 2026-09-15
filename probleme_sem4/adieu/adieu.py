import inflect
p = inflect.engine()

def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            if len(names) == 0:
                continue
            break

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) >= 2:
        print(f"Adieu, adieu, to {p.join(names)}")

main()
