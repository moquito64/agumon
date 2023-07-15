#!/usr/bin/env python3
from colorama import init, Fore, Back, Style
class digimon(object):
    """Digimon Class to make monsters"""
    def __init__(self,name,key):
        self.name = name
        self.hungry = True
        self.key = key
        

class Agumon(digimon):
    def __init__(self,name,key):
        self.name = name
        self.key = key
        pass

def intro():
    print(Fore.RED + "Agumon wakes up slowly and blinks at you with a blank stare")
    print(Fore.YELLOW + "Agumon: Who are you?")
    partner_name = input(Fore.RED + "Enter you name: ")
    print(Fore.YELLOW + "Agumon: Hello " + partner_name + " its nice to meet you finally.")

if __name__ == "__main__":
    intro()