#Make a bank adder that adds deposit to you account 


myName = input("What is your name?: ")
counter = 0
while True:
    deposit = int(input("How much to add? "))
    counter += deposit
    print(myName, "your current balance is $",counter)
    res = input("Do you want to add another deposit? ")
    if res == "No":
        break
print(myName, "thank you for banking with us, the total balance of your account is $",counter)