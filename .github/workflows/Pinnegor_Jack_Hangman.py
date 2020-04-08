import random

#Word list
words = ['rarely','universe','notice','sugar','interference','constitution',
'we','minus','breath','clarify','take','recording','amendment','hut','tip''logical',
'cast','title','brief','none','relative','recently','detail','port','such','complex',
'bath','soul','holder','pleasant','buy','federal','lay','currenty','saint','for','simple',
'deliberately','means','peace','prove','sexual','chief','department','bear','injection',
'off','son','reflect','fast','ago','education','prison','birthday','variation',
'exactly','expect','engine','difficulty','apply','hero','contemporary','that',
'surprised','fear','convert','daily','yours','pace','shot','income','democracy',
'albeit','genuinely','commit','caution','try','membership','elderly','enjoy',
'pet','detective','powerful','argue','escape','timetable','proceeding','sector',
'cattle','dissolve','suddenly','teach','spring','negotiation','solid','seek',
'enough','surface','small','search'.lower()
]
#title
print("Welcome to Hangman! You have 7 lives to guess the answer.")

#word generator
hidden_word = random.sample(words,1)

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
