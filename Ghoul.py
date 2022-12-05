# Для настоящий гулей

from colorama import init
import time
from colorama import Fore, Back, Style

a = 1000

while a >= 0:
    time.sleep(0.09)
    a = a - 7
    print(a)
    if a == -1:
        print(Fore.RED + "\nЯ - гуль, вопросы ?")

input()