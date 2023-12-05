
import datetime

def salutation():
    heure = datetime.datetime.now().hour
    if 5 <= heure < 12:
        return "Bonjour"
    elif 12 <= heure < 18:
        return "Bonjour"
    else:
        return "Bonsoir"

def main():
    print(salutation())

    while True:
        entree_utilisateur = input("Entrez quelque chose (ou 'exit' pour quitter) : ")

        if entree_utilisateur.lower() == 'exit':
            break

        entree_inverse = entree_utilisateur[::-1]
        if entree_utilisateur == entree_inverse:
            print("Bien dit !")
        else:
            print(entree_inverse)

    print("Au revoir")

if __name__ == "__main__":
    main()
