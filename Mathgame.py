#Math Game!
#Name your multiples: 7
#1 X 7 = 7
#Great work! 
#2 X 7 = 14
#Awesome!
#3 X 7 = 54
#Nope. The answer was 21. 
#---
#You scored 3 out of 10.

correct = 0
multi = int(input("Name your multiples: "))
for table in range(1,11):
    print(table, "*", multi)
    result = int(input("=: "))
    if result == multi * table:
        print("Great Work!")
        correct += 1 #If you want to record this answer
    else:
        print("Nope. The answer is", multi * table)
print("You scored",correct, "out of 10")