# In this program I'll demonstrate the use of the 'for' loop, slicing,
# and tuples

# The overall program I'll create is one that will select a word or a string
# element of a tuple and then scramble the word and then have the user attempt
# to guess what the word is and let them know how many attempts it took

# importing the random module to have access to its functions
import random

# I create a tuple which is a sequence of strings. The tuple is also a constant
# which means I don't intend on ever changing the contents of the tuple
WORDLIST = ('street','lazy','apple','orange','science')

# I create a variable called 'word' that will store the randomly chosen
# word from the word list I previously created for the user to decipher

# the choice() function picks a random element from the sequence
word = random.choice(WORDLIST)

# I create a new variable and assign it an empty string to then modify later
# by extracting letters from the randomly chosen word above and add it to the
# end of my new scrambled word
scramble = ""

# I create a 'guesses' variable to count the guess attempts by the user to allow
# for guess count keeping
guesses = 1

# the 'correct' variable will be used later to determine if the guess from
# the user matches the unscrambled word
correct = word

# I create a while loop to continue 'removing' letters randomly from my
# original word and adding them to the end of my new scrambled word until my
# original word is an empty string
while word:

    # I chose a random place to index the original word based on the length
    # of the original utilizing the randrange() function
    position = random.randrange(len(word))

    # I take my scambled word and add the letters i'm taking from the original
    scramble += word[position]

    # here I take my original word and add everything to my new 'orginal' word
    # by slicing everything except the chosen letter that was used to index
    #
    # the reason I have to concetate like this is because of the immutability of
    # strings in Python
    word = word[:position] + word[(position + 1):]

# now I inform the user the rules of the game and then prompt for guesses
# while keeping count of the guesses
print(
"""
\t\tWelcome to Word Jumble!

  In this game you will be given a scrambled word
  and you'll have to guess the correct word!

  You number of attempts will be recorded!  

"""
)

print("\tThe word you will be unscrambling is", scramble)

# here I take the inputted guess and compare if it matches the original word
guess = input("\nYour Guess: ")
while guess != correct:
    print("Sorry that guess was incorrect!")
    
    # here I keep count of the guesses it took until guess == true
    guesses += 1
    guess = input("\nInput another guess: ")

# I finally announce they have correctly guessed the word and show them the
# number of attempts it took
if guess == correct:
    print("\nCongratulations you guessed the word!! ")
    if guesses > 1:
        print("It took you", guesses, "guesses!!")
    else:
        print("It took you", guesses, "guess!!")


    

    

    
    



