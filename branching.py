# The branching program
# In this program I will demonstrate the use of 'if' and 'else' statements
# and the 'while' loop

# First I import the random module to have access to its functions
import random

# To start, the user will be prompted to the rules of the game
print("Let's play a game!\n")
print("I'm think of a number from 1 to 100")
print("How many tries will it take you?")

# Now I will invoke the random module and its random number generator
# To have a number to compare in my condition statements
the_number = random.randint(1, 100)

# Next I will initialize some variables to utilize in my condition statements
# and manipulate them over time using a while loop to keep playing the game
guess = int(input("Take a guess... "))
tries = 1

# I start my loop
while guess != the_number:

    if guess > the_number:
        print("Your guess is too HIGH!")
    else:
        print("Your guess is too LOW!")

    # I continue to ask for guesses while the loop continues
    guess = int(input("Enter your guess... "))

    # update the 'tries' counter every attempt
    tries += 1

# Display the results!    
print("Congratulations!! It took you", tries, "tries!")    
    
    


