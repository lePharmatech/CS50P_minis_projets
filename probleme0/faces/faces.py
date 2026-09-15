def main():
    #Saisie de l'utilisateur
    saisie = input("Message: ")
    print(convert(saisie))

def convert(texte):
    return texte.replace(":)", "🙂").replace(":(", "🙁")

main()
