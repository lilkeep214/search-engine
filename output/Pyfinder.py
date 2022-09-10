from time import sleep
import pyprog
from pyprog import random_links_twitter, prog
import Pylife
from Pylife import alive, i_m_a
import pyhookstyle
from pyhookstyle import *
import os
import colorama
from colorama import Fore
import linkedinsearcher
from linkedinsearcher import linkedin
import google_research
from google_research import rechercher

def finder():
    os.system("pip install colorama")
    alive()
    sleep(0.1)
    os.system("cls")
    welcome_screen()
    
    while True:
        i_m_a()
        choice = input("github finder = 1, facebook finder = 2, twitter finder = 3 / twitter publication finder  = 4 / nitro gen = 5 / linkedin = 6 / recherche = 7 -> ")
        i_m_a()
        if choice == "1":

            name = input("[N]: ")
            find = f"https://github.com/{Fore.RED}{name}"
            print(find)
            input("")
        
        if choice == "2":

            name = input("[N]: ")
            find = f"https://www.facebook.com/{Fore.RED}{name}"
            print(find)
            input("")

        if choice == "3":

            name = input("[N]: ")
            find = f"https://twitter.com/{Fore.RED}{name}"
            print(find)
            input("")
        
        if choice == "4":
            random_links_twitter()
        
        if choice == "5":
            while True:
                prog()


        if choice == "6":
            linkedin()

        if choice == "7":
            rechercher()