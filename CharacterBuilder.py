#Write a subroutine that generates a character, ask the character 
# to supply first name and the character type, write a subroutine 
# that multiplies together a bunch of random dice rolls to create 
# the health stat of the character, write another subroutine that 
# generate a strength stat for the character, using a menu that uses 
# time.sleep and os.system("clear") to make it a really nice way of b
# uilding characters, wrap it in loop to keep asking the user if they 
# want to create another character, and if they do, clear the screen 
# and start over.

#Character Builder

#Name your legend:
#Character type (Human, Elf, Wizard, Orc):

#Your character, , the , has , health and , strength.


import random, os, time

human = "Human"
elf = "Elf"
wizard = "Wizard"
orc = "Orc"

def subroutine():
    os.system("clear")
    while True:
        print("Welcome to Character Builder!\n")
        time.sleep(1)
        os.system("clear")
        charName = input("Name your legend: ")
        os.system("clear")
        charType = input("what is the character type? ")
        os.system("clear")
        strength = random.randint(1,6) * random.randint(1,12) / random.randint(1,2) + 12
        health = random.randint(1,6) * random.randint(1,12) / random.randint(1,2) + 10
        # return (strength)
        if charType == human:
            print("Your legend name is", charName, "\nCharacter type is",human,"\nHEALTH:", health, "\nSTRENGTH:", strength,"\n")
        elif charType == elf:
            print("Your legend name is", charName, "\nCharacter type is",elf,"\nHEALTH:", health, "\nSTRENGTH:", strength,"\n")
        elif charType == wizard:
            print("Your legend name is", charName, "\nCharacter type is",wizard,"\nHEALTH:", health, "\nSTRENGTH:", strength,"\n")
        elif charType == orc:
            print("Your legend name is", charName, "\nCharacter type is",orc,"\nHEALTH:", health, "\nSTRENGTH:", strength,"\n")
        else:
            print("Your character does not exist")
        another = input("Do you want to check another legend?: ")
        if another == "Yes" or "yes":
            os.system("clear")
            continue
        else:
            break
            exit()
subroutine()


