'''
Create a python program in which the user selects a particular
range of number (example 20 to 80 or 330 to 430). The system
should automatically select some random number and the user
must identify that number selected by the system in minimum number of guesses.

If the user identifies it in the required number of guesses then it
should print "Yeah! You identified the number"

else if the number guessed by the user is higher than the randomly
selected number then it should print
"Please try again! The number you guessed is too high"

else if he number guessed by the user is smaller than the randomly
selected number then it should print
"Please try again! The number you guessed is too small".

Else if the user does not guess the integer in minimum number of guesses, then it should
give "Oops! All you chances are finished. Better luck next time!"
'''

import random

min_range = int(input("Enter the minimum range : "))
max_range = int(input("Enter the maximum range : "))

random_number = random.randint(min_range,max_range)

print("You have 5 lives to guess correct number!")

max_life = 5

print("Game starts Now! ")

while max_life > 0:

    guess_num = int(input("Enter the number you guessed : "))

    if (guess_num > max_range) or (guess_num < min_range):
        print("Entered number is out of range.")
    elif guess_num == random_number:
        print("Yeah! You identified the number")
        break
    elif guess_num < random_number :
        print("Please try again! The number you guessed is too small")
    elif(guess_num > random_number) and (max_life > 1) :
        print("Please try again! The number you guessed is too high")
    else :
        print( "Oops! All your chances are finished. Better luck next time!")

    max_life -= 1
