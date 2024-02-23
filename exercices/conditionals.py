"""
Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""

# correctAnswer = 4
# while True:
#     numberInput = int(input("Guess a Number from 1 - 9: "))
    
#     if numberInput == correctAnswer:
#         print("Well guessed!")
#         break
#     else:
#         print("Wrong guess. Try again.")


import random

# Generate a random number between 1 and 10 (inclusive) as the target number
# target_num, guess_num = random.randint(1, 10), 0
# print(target_num)
# print(guess_num)

# # Start a loop that continues until the guessed number matches the target number
# while target_num != guess_num:
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))

# print('Well guessed!') 

# Write a Python program that accepts a word from the user and reverses it.

# word = input("Input a word to reverse: ")

# for char in range(len(word) - 1, -1, -1):
#     print(word[char], end="")

# Write a Python program to count the number of even and odd numbers in a series of numbers.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
countOdd = 0
countEven = 0

for x in numbers:
    if not x % 2:
        countEven += 1
    else:
        countOdd += 1

print("number of even numbers:", countEven)
print("number of odd numbers:", countOdd)

# Write a Python program that accepts a string and calculates the number of digits and letters.

# Prompt the user to input a string and store it in the variable 's'

s = input("Input a string")

d = l = 0

for c in s:
    if c.isdigit():
        d = d + 1
    elif c.isalpha():
        l = l + 1
    else:
        pass

print("Letters", l)
print("Digits", d)




