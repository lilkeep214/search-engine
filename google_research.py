from enum import auto
import random
import string
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def rechercher():
    choix = input("1 - Recherche normal\n2 - recherche random\n3 - recherche google drive\n4 - recherche d'ip\n\n[?]: ")

    if choix == "1":
        recherce1 = input("[S]=> ")

        resultat = f"https://www.bing.com/{Fore.LIGHTGREEN_EX}search?q={Fore.RED}{recherce1}"
        print(resultat)
    
    if choix == "2":
        recherche_starter = int(input("nombre de recherches => "))
        nombre1 = int(input("Nombre de caractères -> "))

        for i in range(recherche_starter):
            recherche2 = "" + "".join(random.choices(string.ascii_letters + string.digits, k=nombre1))
            res = f"https://www.bing.com/{Fore.LIGHTGREEN_EX}search?q={Fore.RED}{recherche2}"
            print(res)
    
    if choix == "3":
        recherche3 = input("[S]=> ")
        resultat2 = f":site google drive:{Fore.RED} {recherche3}"
        print(resultat2)
    
    if choix == "4":
        recherce4 = input("Entrez une IP -> ")
        resultat3 = f"https://www.bing.com/{Fore.LIGHTGREEN_EX}search?q={Fore.RED}{recherche3}"
        print(resultat3)
    

