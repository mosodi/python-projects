#Task, Write a code that ask the kids what animal do they want and respond to them with the sound and ask them to exit
# All this using a Whole loop

animal = input("What animal do you want to hear the sound?: ")
while animal == "Cow":
    cow = "A cow goes meohhhhhhwwwww"
    print(cow)
    stop = input("Stop?: ")
    if stop == "Yes" or "yes":
        exit()
while animal == "Cat":
    cat = "A cat goes mewwwwwwww!!"
    print(cat)
    stop = input("Stop?: ")
    if stop == "Yes" or "yes":
        exit()
while animal == "Dog":
    dog = "A dog goes whoof whoof"
    print(dog)
    stop = input("Stop?: ")
    if stop == "Yes" or "yes":
        exit()
if animal not in ("Cat", "Dog", "Cow"):
    print("Sorry, I only know Cat, Dog and Cow sounds")
    