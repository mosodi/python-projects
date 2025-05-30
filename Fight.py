# ⚔️ BATTLE TIME ⚔️
# Name your Legend:
# Arthur the Magnificent
# Character Type (Human, Elf, Wizard, Orc): 
# Elf
# Arthur the Magnificent
# HEALTH: 13
# STRENGTH: 18
# Who are they battling?
# Name your Legend:
# Sheila the Almighty
# Character Type (Human, Elf, Wizard, Orc): 
# Human
# Sheila the Almighty
# HEALTH: 40
# STRENGTH: 26
# *clear screen here*
# ⚔️ BATTLE TIME ⚔️
# The battle begins!
# Arthur wins the first blow
# Sheila takes a hit, with 8 damage
# Arthur the Magnificent
# HEALTH: 13
# Sheila the Almighty
# HEALTH: 32
# And they're both standing for the next round!
# *clear screen here*
# ⚔️ BATTLE TIME ⚔️
# The battle continues!
# Sheila wins round 2
# Arthur takes a hit, with 8 damage
# Arthur the Magnificent
# HEALTH: 5
# Sheila the Almighty
# HEALTH: 32
# And they're both standing for the next round!
# *clear screen here*
# ⚔️ BATTLE TIME ⚔️
# The battle continues!
# Sheila wins round 3
# Arthur takes a hit, with 8 damage
# Arthur the Magnificent
# HEALTH: -3
# Sheila the Almighty
# HEALTH: 32
# Oh no Arthur the Mighty has died!
# Sheila the Almighty destroyed Arthur the Magnificent in 3 rounds!

import random, os, time

os.system("clear")

legend = input("Name your Legend: ")
char_type = input("Character Type (Human, Elf, Wizard, Orc): ")

def generate_stats():
    health = random.randint(1, 6) * random.randint(1, 12) // random.randint(1, 2) + 10
    strength = random.randint(1, 6) * random.randint(1, 12) // random.randint(1, 2) + 12
    return health, strength

def fight(legend, char_type):
    if char_type not in ["Human", "Elf", "Wizard", "Orc"]:
        print("Your character does not exist.")
        return

    health, strength = generate_stats()
    print(f"\nYour legend name is {legend}")
    print(f"Character type: {char_type}")
    print(f"HEALTH: {health}")
    print(f"STRENGTH: {strength}\n")

    time.sleep(2)
    os.system("clear")

    while True:
        print("The battle begins!\n")
        time.sleep(2)
        os.system("clear")

        print("Arthur the Magnificent")
        print(f"HEALTH: {health}")
        print(f"STRENGTH: {strength}")
        time.sleep(2)
        os.system("clear")

        opponent = input("Who are they battling?\n")
        if opponent != "Sheila the Almighty" and opponent != "Arthur the Magnificent":
            print("Invalid opponent.\n")
            time.sleep(2)
            os.system("clear")
            continue

        sheila_health, sheila_strength = generate_stats()
        print("Sheila the Almighty")
        print(f"HEALTH: {sheila_health}")
        print(f"STRENGTH: {sheila_strength}")
        time.sleep(2)
        os.system("clear")

        round_num = 1
        while health > 0 and sheila_health > 0:
            print(f"Round {round_num}")
            round_num += 1

            if random.choice([True, False]):
                damage = random.randint(1, strength)
                sheila_health -= damage
                print(f"Arthur strikes! Sheila takes {damage} damage.")
            else:
                damage = random.randint(1, sheila_strength)
                health -= damage
                print(f"Sheila strikes! Arthur takes {damage} damage.")

            print(f"\nArthur's HEALTH: {max(0, health)}")
            print(f"Sheila's HEALTH: {max(0, sheila_health)}\n")

            time.sleep(2)
            os.system("clear")

        if health <= 0:
            print("Oh no! Arthur the Mighty has fallen!")
            print(f"Sheila the Almighty destroyed {legend} in {round_num - 1} rounds!")
        else:
            print("Victory! Sheila the Almighty has been defeated!")
            print(f"{legend} wins in {round_num - 1} rounds!")

        break  # End the game after one battle

# Start the game
fight(legend, char_type)
