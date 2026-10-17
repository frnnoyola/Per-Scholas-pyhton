#Requires colorama; install with: pip install colorama


import colorama
from colorama import Back, Fore, Style

print(Fore.RED + "this text is red" + Style.RESET_ALL)
print(Back.YELLOW + Fore.BLACK + 'black text on a yellow background' + Style.RESET_ALL)
print(Style.DIM + 'Dim text' + Style.RESET_ALL)