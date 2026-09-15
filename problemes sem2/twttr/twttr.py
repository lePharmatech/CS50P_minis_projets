def main():
    s = input("Input: ")

    for c in s:
        if c in ["a","e","i","o","u","A","E","I","O","U"]:
                s = s.replace(c,"")
    print(f"Output: {s}")

main()

