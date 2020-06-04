#Jack Pinnegor Hangman Game

import random

with open("words_list.txt") as f:
    word_list = f.read().splitlines()

#title
print("Welcome to Hangman! You have 7 lives to guess.")

#word generator
hidden_word = random.sample(word_list,1)

if(hidden_word[0]):
    print("The length of the word is: " , len(hidden_word[0]))

#parameters
guesses=0
guessed = []
word = []

#Game
for x in range(len(hidden_word[0])):
    word.append(' * ')

while guesses < 7:
    guess = input("Please enter your next guess: ""\n")

    if(guess in hidden_word[0]):
        print("The letter is correct.")
        for index, letter in enumerate(hidden_word[0]):
            if letter == guess:
                word[index] = guess
        guessed.append(guess)

    else:
            print("That letter is incorrect.")
            guesses=guesses+1
            guessed.append(guess)

    print("Please enter your next guess:")
    print("So far, you have answered - %s"%''.join(word))
    print()

    if ''.join(word) == hidden_word[0]:
        break

#Game finish
if guesses==7:
    print("You lose. The word was:" , hidden_word[0])
else:
    print("Congratulations, you won!")
