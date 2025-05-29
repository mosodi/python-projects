#Calculate how many seconds are in a year and ask the user if its a leap year, then calculate it based on the answer
secs_in_a_year = 60*60*24*365
secs_in_a_leap_year = 60*60*24*366
userInput = input("What should I calculate? ")
if userInput == "How many seconds are in a year?":
    print("Is it a leap year?: ")
    answer = input(" ")
    if answer == "Yes":
        print("There are ",secs_in_a_leap_year, "seconds in a leap year")
    else:
        print("There are ",secs_in_a_year, "seconds in a year")


