# This program comes up with a random number, that the user has to guess in 6 trys.

import random  # Imports random module.

guessesTaken = 0  # Assings 0 to guessesTaken variable.

print('Hello! What is your name?')  # Asks for user's name.
myName = input()  # Assigns user's name to myName variable.

number = random.randint(1, 20)  # Assigns a random number between 1 and 20 to number variable.
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Prints.

while guessesTaken < 6:  # While loop that goes as long as guessesTaken is less than 6.
    print('Take a guess.')  # Asks for user to guess the number.
    guess = input()  # Assigns user input to guess vriable.
    guess = int(guess)  # Converts guess into integer.

    guessesTaken += 1  # Adds 1 to guessesTaken.

    if guess < number:  # If guess is lower than number.
        print('Your guess is too low.')  # Prints.

    if guess > number:  # If guess is higher than number.
        print('Your guess is too high.')  # Prints.

    if guess == number:  # If guess is equal to number.
        break  # Breaks out of the while loop.

if guess == number:  # If guess is same as number.
    guessesTaken = str(guessesTaken)  # Converts guessesTaken to string.
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Prints congratulations message with user's name and number of guesses taken.

if guess != number:  # If guess does not match number.
    number = str(number)  # Converts number to string.
    print('Nope. The number I was thinking of was ' + number)  # Prints message with the number the user didn't manage to guess.
