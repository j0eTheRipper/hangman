from random import choice
import words


class Randword:
    def __init__(self, wordlist):
        self.word = choice(wordlist)
        self.blanks = str()
        for i in self.word:
            if i == ' ':
                self.blanks += ' '
            else:
                self.blanks += '-'