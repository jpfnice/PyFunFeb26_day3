"""
Write a Python scripts that implements the “Guess the Number” game.
The script will generate of a random integral number (use the module random) from 1 to 100, and ask you to guess it.

The script will tell you if each guess is too high or too low.
You win if you can guess the number within six tries.

This version of the script uses an exception handler to detect an invalid user input.
"""

import random

# To generate an int in the range [1,100]:
secret=random.randint(1,100)

print(secret) # For testing purpose only ...

# This variable is used to count the number of attempts
# to guess the number :
attempts=1 

while attempts <= 6: # The maximum number of attempts is 6!
    while True:
        try:
            value=int(input(f"Enter an int between [1,100] ({attempts},6): "))
            break # If I reach this statement, it means no exception
            # have been raised, no need to loop on input() anymore
        except ValueError as e:
            print("A ValueError is detected:", e)
            

    if value < secret:
        print(value, "is too small!")
    elif value > secret:
        print(value, "is too large!")
    else:
        print("Bingo !", value, "was the secret number!")
        break # The secret number is found, I can leave the loop
    
    #attempts = attempts + 1 # to increment the number of attempts
    attempts += 1
    
# I may leave the loop because the number has been found or 
# because I've reached the maximum number of attempts.
# I need to test that:
    
if attempts > 6:
    print("The secret number was:", secret)


