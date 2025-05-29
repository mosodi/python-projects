#Create a program that asks the user what number to start with, what number to end with and what increament to use and print that



start = int(input("What is the starting number? "))
end = int(input("What is the ending number? "))
increment = int(input("What is the increment "))
for display in range(start,end, +increment):
    print(display)