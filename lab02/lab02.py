""" Write a function that accepts two arguments (length, start) to generate an array
    of a specific length filled with integer numbers increased by one from start. """

# def generateArray (length , start):
#     arr = [start]
#     for i in range(length):
#         arr.append(arr[i]+1)
#     return arr 
# print(generateArray(5,10))


""" write a function that takes a number as an argument and if the number divisible by 3 
    return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both 
    return "FizzBuzz" """

# def isdivisible(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     elif num % 5 == 0:
#         return "buzz"

# print(isdivisible(5))


""" Write a function which has an input of a string from user then it will return the same string reversed."""

# def reverseString ():
#     str = input("enter the string: ")
#     return str[::-1]

# print(reverseString())




""" Ask the user for his name then confirm that he has entered his name(not an empty string/integers). then proceed to ask him for
his email and print all this data (Bonus) check if it is a valid email or not """
import re

# def validateEmail (email):
#     regex = '^\w+[\w\.-]*@\w+[\w\.-]+\.\w{2,}$'
#     if re.match(regex,email):
#         return True
#     else:
#         return False
    

# def confirmInfo ():
#     name = ""
#     email = ""
#     while True:
#         name = input("enter your name: ")
#         if not name:
#             print("invalid you enterd empty name")
#         elif name.isdigit():
#             print("invalid you enterd a integer ")
#         else :
#             break
#     while True:
#         email = input("enter your email: ")
#         if  validateEmail(email):
#             print(f"hello {name} your email is {email}")
#             return True
#         else:
#             print("invalid email ")
    
# print(confirmInfo())




""" Write a function that takes a string and prints the longest alphabetical ordered substring occurred For example, if
the string is 'abdulrahman' then the output is: Longest substring in alphabetical order is: abdu"""


# def longestAlpha ():
#     name = input("Enter your name: ")
#     currentSubString = name[0]
#     longest = ""
#     for i in range(1,len(name)) :
#         if name[i] >= name[i-1]:
#             currentSubString+= name[i]
#         else:
#             if len(currentSubString) > len(longest):
#                 longest = currentSubString

#             currentSubString = name[i]

#     if len(currentSubString) > len(longest):
#             longest = currentSubString     

#     return longest

# print(longestAlpha())


"""

Write a program which repeatedly reads numbers until the user
enters “done”.

Once “done” is entered, print out the total, count, and
average of the numbers.
If the user enters anything other than a number, detect their
mistake, print an error message and skip to the next number.

"""


# def sumAndAvg():
#     numbers = []
#     while True:
#         userInput = input("Enter your number: ")
#         if userInput == "done":
#             break
#         try:
#             numbers.append(float(userInput))    
#         except ValueError:
#             print("enter number ")

#     if len(numbers) == 0:
#         print("No numbers entered.")
#     else:
#         count = len(numbers)
#         total = sum(numbers)
#         avg = total / count
#     return total,avg,count

# print(sumAndAvg())



"""

Word guessing game (hangman)
○
A list of words will be hardcoded in your program, out of
which the interpreter will
○choose 1 random word.
○The user first must input their names
○
Ask the user to guess any alphabet. If the random word
contains that alphabet, it
○will be shown as the output(with correct placement)
○Else the program will ask you to guess another alphabet.
○Give 7 turns maximum to guess the complete word.



"""
# import random
# def guessingGame ():

#     word_list = ["apple","car","bus","iti","box"]

#     # Select a random word
#     word = random.choice(word_list)

#     # Set up the game
#     max_guesses = 7
#     current_guesses = 0
#     correct_guesses = set()
#     incorrect_guesses = set()

#     # Get the user's name
#     name = input("What is your name? ")

#     # Play the game
#     while True:
#         # Display the word with underscores for unguessed letters
#         display_word = ""
#         for letter in word:
#             if letter in correct_guesses:
#                 display_word += letter
#             else:
#                 display_word += "_"
#         print(display_word)

#         # Ask the user to guess a letter
#         guess = input("Guess a letter: ").lower()

#         # Check if the letter has already been guessed
#         if guess in correct_guesses or guess in incorrect_guesses:
#             print("You already guessed that letter. Try again.")
#             continue

#         # Check if the letter is in the word
#         if guess in word:
#             print(f"Good guess! ")
#             correct_guesses.add(guess)
#             # current_guesses += 1
#         else:
#             print("Sorry, that letter is not in the word.")
#             print(f"your still turns is {max_guesses - current_guesses -1 }")
#             incorrect_guesses.add(guess)
#             current_guesses += 1

#         # Check if the user has won or lost
#         if set(word) <= correct_guesses:
#             print(f"Congratulations, {name}! You won!")
#             break
#         elif current_guesses >= max_guesses:
#             print(f"Sorry, {name}. You lost. The word was {word}.")
#             break



# guessingGame()
