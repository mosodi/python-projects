#Create an OTP random number generator that give the user random numbers everytime the run

def otp(numbers):
    import random
    code = " "
    for n in range(numbers):
        code += str(random.randint(0,9))
    return(code)
generate = otp(6)
print("Your OTP code is",generate)

