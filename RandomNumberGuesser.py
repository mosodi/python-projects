#Generate random numbers between 1 to a million, and display the correct number

import random

correct = 0
num = random.randint(1,10)
for i in range(num):
    enter = int(input("Guess a number from 1 to 1 million: "))
    correct += 1
    if enter < num:
        print("Too low! Try again!")
    elif enter > num:
        print("Too high! Try again!")
    else:
        print("Yay!!! Correct,", num,"is the correct number")
        print("It took you", correct, "guesses to get the right number")
        break
