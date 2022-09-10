import random
import string
import colorama
from colorama import Fore

def linkedin():
    name = input("[N]")
    choix = input("Voulezz voux cherchez des comptes spam ? (O/N) ")

    if choix == "O":
        for i in range(4001):
            lien = f"https://www.linkedin.com/{Fore.LIGHTGREEN_EX}in{Fore.WHITE}/{Fore.RED}{name}{i}"
            print(lien)
        choix3 = input("Voulez vous plus de résultats ? [O/N]: ")
        if choix3 == "O":
            choix4 = input("Voulez vous chercher toute le possibilité ? [O/N]: ")
            if choix4 == "O":
                choix5 = int(input("Combien de caractères -> "))
                while True:
                    spam_account = "" + "".join(random.choices(string.ascii_lowercase, k=choix5))
                    result2 = f"https://www.linkedin.com/{Fore.LIGHTGREEN_EX}in{Fore.WHITE}/{Fore.RED}{spam_account}"
                    print(result2)
            if choix4 == "N":
                choix7 = int(input("Combien de caractères -> "))
                choix6 = int(input("Combien de comptes ? -> "))
                for i in range(choix6):
                    spam_account = "" + "".join(random.choices(string.ascii_lowercase, k=choix7))
                    result1 = f"https://www.linkedin.com/{Fore.LIGHTGREEN_EX}in{Fore.WHITE}/{Fore.RED}{spam_account}"
                    print(result1)
        if choix3 == "N":
            print("Redirection...")
    if choix == "N":
        choix2 = input("Voulez vous chercher une companie ou un utilisateur ? (com/user) ")

        if choix2 == "com":
            link = f"https://www.linkedin.com/{Fore.LIGHTGREEN_EX}company{Fore.WHITE}/{Fore.RED}{name}"
            print(link)


        if choix2 == "user":
            user = f"https://www.linkedin.com/{Fore.LIGHTGREEN_EX}in{Fore.WHITE}/{Fore.RED}{name}"
            print(user)