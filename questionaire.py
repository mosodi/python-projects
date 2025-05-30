#Write a program that will ask the user what they think about the challenge so far and for each response, tell them something


for i in range(1,31):
    userInput = input("What do you feel about the 30 days of this challenge so far?: ")
    print(f"{i} of 100 was {userInput: ^2}")