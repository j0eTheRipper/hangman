# Write your code here
import random
from words import words

whileHolder = True


def hangman():
    randword = words[random.randint(0, len(words) - 1)]
    blanks = '-' * len(randword)
    tries = set()
    lives = 8
    not_ascii = '~!@#$%^&*()_+`1234567890-=[]\\{}|;\':",./<>?'
    while lives > 0:
        print('')
        print(blanks + '   You have', lives, 'lives left')
        guess = input('Input a letter: ')
        if guess in randword and guess not in tries:
            tries.add(guess)
            for j in range(len(randword)):
                if randword[j] == guess:
                    blanks_ = ""
                    blanks = list(blanks)
                    blanks[j] = guess
                    for x in blanks:
                        blanks_ += x
                    blanks = blanks_
            if randword == blanks:
                print('')
                print(blanks)
                print('You guessed the word!')
                print('You survived!')
                break
        elif guess in tries:
            print('You already typed this letter')
        elif len(guess) == 1 and (guess.isupper() or guess in not_ascii):
            print('It is not an ASCII lowercase letter')
        elif len(guess) != 1:
            print('You should enter a single letter')
        else:
            tries.add(guess)
            print('No such letter in the word')
            lives -= 1
    else:
        print('You are hanged!')


print('H A N G M A N')
while whileHolder:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':
        hangman()
    elif menu == 'exit':
        quit()
    else:
        continue

