from mimetypes import guess_extension
import random

answer = random.randint(1,9)
guessedCorrect = False

while guessedCorrect == False:
    userGuess = int(input('Guess a number from 1-9: '))
    if userGuess < answer:
        print('To low try again')
    elif userGuess > answer:
        print('To high try again')
    elif userGuess == answer:
        print('You guessed correct!')
        guessedCorrect = True