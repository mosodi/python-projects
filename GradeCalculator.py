#Exam grade calculator
#Task: Ask them the name of Exam, the maximum score, their score and tell them what point they got and if its A,B or U


exam = input("What's the Exam? ")
yourScore = float(input("What score did you receive in %? "))
if yourScore < 5:
    print("In your", exam,"Exam, You scored",yourScore,"% out of", maxScore,"Sorry, You failed with an F9")
elif yourScore > 5 or yourScore < 20:
    print("In your", exam,"Exam, You scored",yourScore,"% out of 100% Which is D Grade")
elif yourScore > 20 or yourScore < 40:
    print("In your", exam,"Exam, You scored",yourScore,"% out o f100% Which is E Grade")
elif yourScore > 40 or yourScore < 60:
    print("In your", exam,"Exam, You scored",yourScore,"% out of 100% Which is C Grade")
elif yourScore > 60 or yourScore < 70:
    print("In your", exam,"Exam, You scored",yourScore,"% out of 100% Which is A- Grade")
elif yourScore > 80 or yourScore < 100:
    print("In your", exam,"Exam, You scored",yourScore,"% out of 100% Which is A+ Grade")
else:
    print(yourScore,"is too high, 100% is the max percentage, reduce the score")
