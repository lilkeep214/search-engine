import random
import string
import time
import colorama
from colorama import Fore
from time import sleep

def random_links_twitter():
    name = input("[N]: ")
    num = int(input("How many publication you want -> "))
    for i in range(num):
        publication_ID = "" + "".join(random.choices(string.digits, k=19))
        publication_link_compiler = f"https://twitter.com/{Fore.RED}{name}{Fore.LIGHTCYAN_EX}/status/{Fore.LIGHTGREEN_EX}{publication_ID}{Fore.LIGHTCYAN_EX}/photo/1"
        print(publication_link_compiler)
        sleep(0.1)
    input("")

def prog():
    rdm = "" + "".join(random.choices(string.ascii_letters + string.digits, k=24))
    result = f"{rdm}"
    print(f"https://discord.gift/{Fore.LIGHTGREEN_EX}{result}")
    sleep(0.1)