def main():
    # les entrées et sorties
    camel_case = input("camelCase: ")
    print(f"snake_case: {verification_de_uppercase(camel_case)}")

def verification_de_uppercase(n):
    for i in n:
        if i.isupper():
           m = "_" + i.lower()
           return n.replace(i,m)

    else:
      return n
main()
