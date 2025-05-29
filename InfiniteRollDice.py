#Write a subroutine that rolls a dice and let the user know if its correct or not

def rollDice(a):
    import random
    userInput = int(input("How many sides do you want to roll?: "))
    for i in range(1,userInput):
        diceSides = random.randint(1,userInput)
        print("You Rolled", diceSides)
        userAns = input("Roll Again?: ")
        if userAns == 'Yes':
            continue
        else:
            break
a  = 0
rollDice(a)
