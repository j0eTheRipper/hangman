# Write your code here
import words
from Users import User
from Randword import Randword


user = User(input('Hey bro, enter your name: '))


def end_msg(randword, is_success):
    if is_success:
        user.score_handler(10)
        print('')
        print(randword + '\nYou guessed the word!\nYou survived!\n')
    else:
        print('You are hanged!')
        print('')
        print('The word was', randword)
        print('')


def hangman(wordlist):
    randword = Randword(wordlist)
    tries = set()
    chances = 8

    while chances > 0:
        print('\n' + randword.blanks)
        usr_input = input('Input a letter or the whole word if you guessed it: ').lower()

        if usr_input in randword.word and usr_input not in tries:  # If the guess correct and not repeated
            tries.add(usr_input)

            if randword.word == randword.blanks:  # if the user guessed the hole word
                end_msg(randword.word, True)
                break
            else:
                if len(usr_input) == 1:  # if the user entered a single letter
                    randword.letter_parser(usr_input)
                elif len(usr_input) > 1:  # if the user entered a whole word
                    if usr_input == randword.word:
                        end_msg(randword.word, True)
                        break

        elif usr_input in tries:  # if the input is already written
            print('You already typed this letter')
        elif '/' in usr_input:  # if the input is a command
            if usr_input == '/whiteflag':
                end_msg(randword.word, False)
                break
            elif usr_input == '/chances':
                print(f'you have {chances} chances of living' if chances > 1 else 'you have 1 chance of living')
            elif usr_input == '/help':
                print('/whiteflag if you give up\n/chances to see your chances of living')
            else:
                print('This is not a command')
        elif not usr_input.isalpha():
            print('This is not an English letter')
            continue
        else:  # if the input was an incorrect guess
            tries.add(usr_input)
            chances -= 1
            print(f'you have {chances} chances of living' if chances > 1 else 'you have 1 chance of living')
    else:
        end_msg(randword.word, False)


print(f"\nYo, what's up {user.usr_name}!")
print(f'Your score is {user.score}\n')
while True:
    menu = input('Select an option from the list:\n1: play\n2: show your info\n3: exit\n> ')
    if menu == '1':
        word_menu = input('Select a category from the list:\n1: chemistry\n2: physics\n3: biology\nback\n> ')
        print('Type one letter or the whole word if you guessed it.\n/help for help.')
        if word_menu == '1':
            hangman(words.chemistry)
        elif word_menu == '2':
            hangman(words.physics)
        elif word_menu == '3':
            hangman(words.biology)
        elif word_menu == 'back':
            continue
    elif menu == '2':
        print(f'\n{user.usr_name}, {user.score} pts\n')
    elif menu == '3':
        quit()
    else:
        continue
