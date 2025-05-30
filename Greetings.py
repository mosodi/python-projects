#Create a list that stores a greeting
#in different languages
#Generate a random number between 0 and the max in list
#When you say run, it should randomly greet someone
#in that language

import random

hellos = ["Hello", "Ola", "Obrigado", "Привет", "Bonjour", "你好"]

index = random.randint(0,5)
print(hellos[index])

 