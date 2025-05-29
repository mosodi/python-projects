#Create a music player that lets the user
#Press 1 to play
#Press 2 to Exit
#Press any other button to see the menu


from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  while True:
    select = input("1. Play\n2. Exit\n")
    if select == "1":
      source = audio.play_file('audio.wav')
      print("Playing")
      time.sleep(3)
      os.system("clear")
      continue
    elif select == "2":
      print("Exiting")
      break
    else:
      print("Show the menu again")
play()