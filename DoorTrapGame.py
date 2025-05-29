#Write a door trap game that has one secret door and the user's job is to guess which is the right doorm if the user enters the wrong door, they fall to their death and Game over

while True:
    print("Guess the secret door using this keys L,R,F,B,U,D, Only one door is right")
    rightDoor = input("Make your input ")
    if rightDoor == "F":
        print('Correct the right door was F')
        break
    else:
        print("Try again!")
        continue
print("The Game is Over!")
exit()
