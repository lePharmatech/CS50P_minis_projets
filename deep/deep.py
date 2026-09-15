def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if logique(user_input):
        print("Yes")
    else:
        print("No")

def logique(n):
    if n == "42" or n == "forty-two" or n == "forty two":
        return True
    else:
        return False

main()
