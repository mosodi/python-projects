#Write a code that asks the user their name
#their years of experience
#and if their experience is less that
#zero years, tell them there is no
#opportunity for them in your company
#else offer them some positions
#and tell them you will get back to them

#Nexted if and else statement


print ("Welcome to the interview questions")

user_name = input("What is your name? ")
experience = int(input("How many years of experience do you have "))
if experience < 1:
    print(user_name, "Sorry you don't have any future here")
else:
    print("Congratulations!",user_name,"you have", experience, "years of experience, we can now start the inteview")
    print("Here are your interview questions")
    que = input("Are you a good Python Developer? ")
    if que == "yes" or que == "Yes":
        print("Awesome! How much should we pay you?")
        pay = int(input("Write how much in $$ "))
        if pay < 1000:
            print("Ok,", user_name, " we will pay you", pay, "and we are going to get back to you")
        else:
            print(user_name, "Sorry, we can't pay you ", pay, "right now")
    else:
        print("Sorry", user_name,"we are only looking for Python Developers are the moment")
