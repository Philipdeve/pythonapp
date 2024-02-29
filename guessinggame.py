from guess import *


print("Welcome to  who wants to be a millionaire guessing game")
print("Please You have only 2 guesses")

while guess != hidden_word and not out_of_guesses:
    if guess_count < guess_limit:
       guess = input ("Enter guess: ")
       guess_count += 1
       
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Guessing Limit Exhausted, You lose")
else:
    print("You win")
    print("You have won  a million naira")