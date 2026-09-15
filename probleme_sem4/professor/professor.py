from random import randint


def main():
    level = get_level()
    # print(x, y)
    score = 0


    for i in range(10):
        essaie = 0
        try:
                x = generate_integer(level)
                y = generate_integer(level)
                z = x + y
                a = int(input(f"{x} + {y} = "))
                while a != z:
                    print("EEE")
                    a = int(input(f"{x} + {y} = "))
                    essaie += 1
                    if essaie == 2:
                            print(f"{x} + {y} = {z}")
                            break
                if a == z:
                    score += 1
        except ValueError:
               pass

    print(f"Score: {score}")




def get_level():
    while True:
        try:
          level = int(input("Level: "))
          if (level == 1 or level == 2 or level == 3):
                 break
        except ValueError:
            pass
    # generate_integer(level)
    return level
def generate_integer(level):

        if type(level) != int or level < 0:
                raise ValueError()
        else:
                if level == 1:
                         return randint(0, 9)
                elif level == 2:
                          return randint(10, 99)
                elif level == 3:
                          return randint(100, 999)

if __name__ == "__main__":
    main()
