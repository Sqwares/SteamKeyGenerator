import threading
import random
import time
from colorama import init, Fore
import string
import ctypes
import os

init(convert=True)
ctypes.windll.kernel32.SetConsoleTitleW("Steam Key Generator - By Sqwares#4767")
text='''
 ▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄  ▄▄▄ ..▄▄ ·      ▄▄ • ▄▄▄ . ▐ ▄ 
██· █▌▐█▐█ ▀█ ▀▄ █·▀▄.▀·▐█ ▀.     ▐█ ▀ ▪▀▄.▀·•█▌▐█
██▪▐█▐▐▌▄█▀▀█ ▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
▐█▌██▐█▌▐█ ▪▐▌▐█•█▌▐█▄▄▌▐█▄▪▐█    ▐█▄▪▐█▐█▄▄▌██▐█▌
 ▀▀▀▀ ▀▪ ▀  ▀ .▀  ▀ ▀▀▀  ▀▀▀▀     ·▀▀▀▀  ▀▀▀ ▀▀ █▪
                                                                        
                                                                        
'''

def gen(fix, amount):
    while fix <= amount:
        code = ('').join(random.choices(string.ascii_letters.upper() + string.digits.upper(), k=4))
        code2 = ('').join(random.choices(string.ascii_letters.upper() + string.digits.upper(), k=4))
        code3 = ('').join(random.choices(string.ascii_letters.upper() + string.digits.upper(), k=4))
        f.write(code.upper() + "-" + code2.upper() + "-" + code3.upper() + '\n')
        print(code.upper() + "-" + code2.upper() + "-" + code3.upper())
        fix += 1
        ctypes.windll.kernel32.SetConsoleTitleW("Generated keys: " + str(fix) + "/" + str(amount))

print(Fore.BLUE + text + Fore.WHITE)
f = open('keys.txt', 'a')
print(Fore.BLUE + 'Enter the number of codes to be generated: ')
amount = int(input())
fix=1
gen(fix, amount)

'''
Coding by Sqwares

Contact:

Discord:Sqwares#4767
instagram:@sqwares_

'''
