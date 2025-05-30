#Write a subroutine that writes text in color. All it will do is print out the text in that color and turn the color back to normal when it's finished.

import os,time

def color():
    print("With my", end=" ")
    print("New program \033[0;34m", end=" ")
    print("I can just call red ('and)", end=" ")
    print("and \033[0;31m")
    
color()