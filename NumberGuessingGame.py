#Write a program that will guess the number from 0 and 1,000,000. calculate the number 
#of time it took them to guess it correctly.

counter = 0
while True:
    print("Guess the correct number from 1 - 1,000,000")
    numberGuess = int(input("Your Guess: >  "))
    counter += 1
    if numberGuess < 0:
        print("Number cannot be negative, Game Over!!!")
        exit()
    elif numberGuess < 499999:
        print("Too Low, Try again")
    elif numberGuess > 500000:
        print('Too High, Try Lower')
    else:
        print("Correct, the right number is", numberGuess)
        print("It took you", counter, "times in order for you to get the answer right!")
        break
print("game Over!")
