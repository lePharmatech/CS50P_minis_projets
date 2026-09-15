def main():
    while True:
        try:
            valeur = input("Fraction: ")
            x = int(valeur.split('/')[0])
            y = int(valeur.split('/')[1])
            if x > y or x < 0:
                raise ValueError
            z = round((x/y) * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

    if z <= 1:
        print("E")
    elif z >= 99:
        print("F")
    else:
        print(f"{z}%")


main()
