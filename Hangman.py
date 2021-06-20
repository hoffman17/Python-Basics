# this program will simulate the Hangman game

import random

# I create the visual depictions of what the Hangman looks like at each
# incorrect guess
HANGMAN = (
"""

------
|    |
|
|
|
|
|
|
|
----------
""",
"""

------
|    |
|    0
|
|
|
|
|
|
----------
""",
"""

------
|    |
|    0
|   -+-
|
|
|
|
|
----------
""",
"""

------
|    |
|    0
|   -+-/
|    
|
|
|
|
----------
""",
"""

------
|    |
|    0
|  /-+-/
|    
|
|
|
|
----------
""",
"""

------
|    |
|    0
|  /-+-/
|    |
|
|
|
|
----------
""",
"""

------
|    |
|    0
|  /-+-/
|    |
|    |
|   |
|   |
|
----------
""",
"""

------
|    |
|    0
|  /-+-/
|    |
|    |
|   | |
|   | |
|
----------
""")

# I create a list of random words that will be chosen for the game
WORDS = ("lazy", "strong", "weak", "timid", "diligent")

# I randomly select one word from my above list of words and store in it the
# reference called 'word'
word = random.choice(WORDS)

# I create a reference to represent what letters have been guessed so far
so_far = "-" * len(word)

# I start a counter for how many attempts have been taken
wrong = 0

# I create a reference that will reflect the maximum wrong guesses allowed
max_wrong = len(HANGMAN) - 1

# I create a list where the wrong guesses will be stored
used = []

# Welcome the user
print("Welcome to Hangman. Good Luck!!")

# I create my main loop
while wrong < max_wrong and so_far != word:

    # I show the current depiction of how far the Hangman has come
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    # I gather their guess
    guess = input("\n\nEnter your guess: ")

    # I see if the guess has been used before and if so prompt again
    while guess in used:
        print("You've already guessed this letter", guess)
        guess = input("Enter your guess: ")

    # I add the guess to the list of guesses
    used.append(guess)

    # if the guess is found within the word chosen
    if guess in word:
        new = ""

        #iterate through the word and update the so_far reference to reflect
        #the guessed character
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    #print a catch all if the guess isn't in the word and update the wrong
    #counter
    else:
        print("\nSorry," ,guess, "isn't in the word")
        wrong += 1

# if out of guesses end the game
if wrong == max_wrong:
    print(HANGMAN[wrong])
    print("\nYou've been hanged")

# or congratulate if they successfully guessed the word
else:
    print("\nYou've guessed it!!")

# print the word
print("The word was:", word)
        
    
    







