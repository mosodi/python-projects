from getpass import getpass as input


print("Rock, Paper or Scissors?")
player1 = input("What's your bet? ")
player2 = input("What's your bet? ")
answer1 = "Rock"
answer2 = "Paper"
answer3 = "Scissors"

if player1 == answer1 and player2 == answer2:
    print(player1, "is greater than", player2, "So Player 1 Won")
elif player1 == answer1 and player2 == answer3:
    print(player1, "is greater than", player2, "So Player 1 Won")
elif player1 == answer2 and player2 == answer3:
    print(player1, "is greater than", player2, "So Player 1 Won")
elif player1 == answer2 and player2 == answer1:
    print(player2, "is greater than", player1, "So Player 2 Won")
elif player1 == answer3 and player2 == answer1:
    print(player2, "is greater than", player1, "So Player 2 Won")
elif player1 == answer3 and player2 == answer2:
    print(player2, "is greater than", player1, "So Player 2 Won")
elif player1 != answer1 and player1 != answer2 and player1 != answer3:
    print("Sorry, Player 1,", player1," is not a valid bet, You must type Rock, Paper or Scissors in order to bet")
elif player2 != answer1 and player2 != answer2 and player2 != answer3:
    print("Sorry, Player 2,", player2," is not a valid bet, You must type Rock, Paper or Scissors in order to bet")
else:
    print("The Game was a Tie")
