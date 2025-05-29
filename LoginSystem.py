#Create a simple login system for 
# a website, ask for the username 
# and password and if the username is 
# incorrect let'em know, else log them in

validName = "Martins"
validPass = "Mart1000@"

def login():
    while True:
        userName = input("What is your name?: ")
        passWord = input("Enter password: ")
        if userName == validName or passWord == validPass:
            print("Welcome to the program", userName)
            exit()
        else:
            print("Invalid Credentials, Try again!")
login()


