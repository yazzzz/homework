#!/usr/bin/python

import random
import re

"""
input cases to handle:
q should quit
check spaces 
check letters
check valid number from 1-100
check floats
"""

secret_num = random.randint(1,100)
print secret_num
keepPlaying = True
guess = -1
name = raw_input("what is your name? ")
print "hi %s, i'm thinking of a number between 1 and 100, try and guess it!" % name


while keepPlaying == True:
    guess = raw_input("your guess? " )

    # we need to check for valid input
    # if we find a . in the number, split it to make an int
    guess = guess.split(".")[0]
    if re.findall("\.",guess):  
        print "FYI, converting your guess to ", guess

    if guess.isdigit():
        guess = int(guess)

        if guess > 100 or guess < 1:
            print "woah, that number is out of the 1-100 range!"
        elif guess > secret_num:
            print "too high! try again."
        elif guess < secret_num:
            print "too low! try again."
        elif guess == secret_num:
            print "WINNER WINNER CHICKEN DINNER!"
            answer = raw_input("play again? ")
            if answer.lower() in ["y", "yes"]:
                keepPlaying = True
                secret_num = random.randint(1,100)
                print secret_num
            elif answer.lower() in ["n", "no", "q","quit"]:
                keepPlaying = False

    else:
        print "please enter a valid number!"



