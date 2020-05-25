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
        print('')
        print(randword.blanks)
        guess = input('Input a letter or the whole word if you guessed it: ').lower()

        if guess in randword.word and guess not in tries:
            tries.add(guess)
            if len(guess) == 1:
                for j in range(len(randword.word)):
                    if randword.word[j] == guess:
                        randword.blanks = list(randword.blanks)
                        randword.blanks[j] = guess
                        randword.blanks = ''.join(randword.blanks)
            elif len(guess) > 1:
                if guess == randword.word:
                    end_msg(randword.word, True)
                    break

            if randword.word == randword.blanks:
                end_msg(randword.word, True)
                break
        elif guess in tries:
            print('You already typed this letter')
        elif '/' in guess:
            if guess == '/whiteflag':
                end_msg(randword.word, False)
                break
            elif guess == '/score':
                print('your score is:', user.score)
            else:
                print('This is not a command')
        elif not guess.isalpha():
            print('This is not an English letter')
            continue
        else:
            tries.add(guess)
            chances -= 1
            if chances > 1:
                print('Wrong!', 'You have', chances, 'chances of living!')
            elif chances == 1:
                print('Wrong!', 'You have only', chances, 'chance of living!')
    else:
        end_msg(randword.word, False)


print(f"\nYo, what's up {user.usr_name}!")
print(f'Your score is {user.score}\n')
while True:
    menu = input('Select an option from the list:\n1: play\n2: show your info\n3: exit\n> ')
    if menu == '1':
        word_menu = input('Select a category from the list:\n1: chemistry\n2: physics\n3: biology\n> ')
        print('Type /whiteflag if you give up, /score to show your score')
        if word_menu == '1':
            hangman(words.chemistry)
        elif word_menu == '2':
            hangman(words.physics)
        else:
            hangman(words.biology)
    elif menu == '2':
        print(f'\n{user.usr_name}, {user.score} pts\n')
    elif menu == '3':
        quit()
    else:
        continue
