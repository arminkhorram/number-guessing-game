# for generating a random number
import random

# generating a random number between 1 and 10
random_number = random.randint(1, 10)

def number_guessing_game():
    guess_try = 3

    while True:
        guessed_number = input('Guess a Number between 1 to 10, You have 3 Tries, or Enter stop: ')
        try:
            if int(guessed_number) == random_number:
                print('Correct')
                break

            if int(guessed_number) < random_number:
               print('Higher')
               guess_try = guess_try - 1
               print('You have, ' + str(guess_try) + ' guesses left')

            if int(guessed_number) > random_number:
                print('Lower')
                guess_try = guess_try - 1
                print('You have, ' + str(guess_try) + ' guesses left')

            if guess_try == 0:
                print('You have no more tries')
                return
        except ValueError:
            if guessed_number == 'stop':
                break
            
number_guessing_game()