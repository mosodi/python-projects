#Create 2 subroutines, One will roll a dice of any number and return the number, second subroutine is going to

import random

def sixSides(dice):
    six = " "
    for i in range(dice):
        six += str(random.randint(0,6))
    return(six)
rollDice = sixSides(1)
# print("You rolled",rollDice)

def eightSides(dice2):
    eight = " "
    for i in range(dice2):
        eight += str(random.randint(0,8))
    return(eight)
eightDice = eightSides(1)

warrior1 = "Zoro"
warrior2 = "Commando"
warrior3 = "Vandan"

while True:
    takeParam = input("What is your warrior?: ")
    if takeParam == warrior1:
        print(warrior1," health is", eightDice,rollDice,"hp")
    elif takeParam == warrior2:
        print(warrior2," health is", eightDice,rollDice,"hp")
    elif takeParam == warrior2:
        print(warrior3," health is", eightDice,rollDice,"hp")
    else:
        print("Your warrior is not in our database")
