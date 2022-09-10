import colorama
import pyfiglet
from colorama import Fore

colorama.init(autoreset=True)

def welcome_screen():
    title = pyfiglet.figlet_format("PYHOOK")
    print(Fore.BLUE + title + "\n")
    print(Fore.RED + "="*100)
    print("module made by : JORAV#4745")
    print(Fore.RED + "="*100)
