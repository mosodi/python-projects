#Subroutine is a function build that allows you to write some codes and call them whenever you need them



def rollDice():
    import random
    dice = random.randint(1,6)
    print("You rolled", dice)
rollDice()