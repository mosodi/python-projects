#Rock Paper Scissors Game in rounds and display the winner after 2nd rounds
from getpass import getpass as input

while True:
  print("Round 1")
  print("Rock, Paper, Scissors, Shoot!")
  player1 = input("Player 1, make your move:")
  # getpass hides the input
  player2 = input("Player 2, make your move:")
  print(f"Player 1: {player1}  Player 2: {player2}")
  if player1 == player2:
    print("It's a tie!")
  elif player1 == "R" and player2 == "S":
    print("Round 2")
    print("Rock, Paper, Scissors, Shoot!")
    player1 = input("Player 1, make your move:")
    player2 = input("Player 2, make your move: ")
    print(f"Player 1: {player1}  Player 2: {player2}")
    if player1 == player2:
      print("It's a tie!")
      print("Game Over")
      break
    elif player1 == "rock" and player2 == "scissors":
      print(f"Player 1 wins! {player1} beats {player2} with 2 rounds")





    

