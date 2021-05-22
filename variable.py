# The variable program
# In this program I'll illustrate how to use variables to store information
# I will get the information by prompting the user and then storing it


# starting from the left to the right, I created a variable titled "name"
# next by utilizing the "=" operator I'm assigning it the value of the
# information to the right of the "=" operator. In this case, I'm invoking
# the input function to prompt the user with a string to gather a particular
# piece of information from them. In this case it is their name. After they
# enter their name and hit the "Enter" key it will be stored into our local
# variable titled "name"
name = input("Hello, what is your name? ")

# now I invoke the print() function and display the name given by the user
print("\nThe name you gave me was,", name)
