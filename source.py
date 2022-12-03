from mailtm import Email
from colorama import init
from colorama import Fore
from colorama import just_fix_windows_console
import pyperclip
from os import system
just_fix_windows_console()
init()

emails = 0
email = ""

def listener(message):
    global emails, email

    emails = emails + 1

    title("[READY - " + str(emails) + " email(s)] mail.tm (" + email + ")")

    print(Fore.GREEN + "\n[New Email]")
    #print(Fore.RESET + ''.join(message))

    print(Fore.LIGHTBLUE_EX + "\n- [Subject]: " + Fore.RESET + message['subject'])
    print(Fore.LIGHTBLUE_EX + "\n- [Content]: " + Fore.RESET + message['text'] if message['text'] else message['html'])

def title(t):
    system("title " + t)

title("[SETUP] mail.tm")

print(Fore.LIGHTBLUE_EX + "[Setup]:")
print(Fore.LIGHTCYAN_EX + "\n[1]: Random email name\n[2]: Choose email name" + Fore.LIGHTMAGENTA_EX)
choice = input(">>> ")

print("\n")

e = Email()

if choice == "1":
    e.register()
elif choice == "2":
    ename = input("[Email Name] >>> ")
    e.register(username=ename)
else:
    print(Fore.RED + "[Invalid option]")
    input()

pyperclip.copy(str(e.address))
email = str(e.address)
title("[READY - 0 email(s)] mail.tm (" + str(e.address) + ")")
print(Fore.LIGHTBLUE_EX + "\n[Email Address]: " + Fore.RESET + str(e.address) + Fore.GREEN + " (Copied to clipboard)")

e.start(listener, interval=3)
print(Fore.LIGHTCYAN_EX + "\n[Waiting for emails...]")
