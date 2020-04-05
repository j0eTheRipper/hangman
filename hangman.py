# Write your code here
import random
import words

whileHolder = True


def end_msg(randword, is_success):
    if is_success:
        print('')
        print(randword + '\nYou guessed the word!\nYou survived!')
    else:
        print('You are hanged!')
        print('')
        print('The word was', randword)
        print('')


def blanks_parser(randword, blanks):
    for i in randword:
        if i == ' ':
            blanks += ' '
        else:
            blanks += '-'


def hangman():
    randword = random.choice(words.physics)
    blanks = ''
    tries = set()
    chances = 8
    not_ascii = '~!@#$%^&*()_+`1234567890-=[]\\{}|;\':",./<>?'
    blanks_parser(randword, blanks)

    while chances > 0:
        print('')
        print(blanks)
        guess = input('Input a letter or the whole word if you guessed it: ').lower()
        if guess in randword and guess not in tries:
            tries.add(guess)
            if len(guess) == 1:
                for j in range(len(randword)):
                    if randword[j] == guess:
                        blanks = list(blanks)
                        blanks[j] = guess
                        blanks = ''.join(blanks)
            elif len(guess) > 1:
                if guess == randword:
                    end_msg(randword, True)
                    break
            if randword == blanks:
                end_msg(randword, True)
                break
        elif guess in tries:
            print('You already typed this letter')
        elif guess in not_ascii:
            print('This is not an English letter')
        else:
            tries.add(guess)
            chances -= 1
            if chances > 1:
                print('Wrong!', 'You have', chances, 'chances of living!')
            elif chances == 1:
                print('Wrong!', 'You have only', chances, 'chance of living!')
    else:
        end_msg(randword, False)


print('H A N G M A N')
while whileHolder:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':
        hangman()
    elif menu == 'exit':
        quit()
    else:
        continue

