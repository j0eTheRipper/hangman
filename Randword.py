from random import choice


class Randword:
    def __init__(self, wordlist):
        self.word = choice(wordlist)
        self.blanks = str()
        for i in self.word:
            if i == ' ':
                self.blanks += ' '
            else:
                self.blanks += '-'

    def letter_parser(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.blanks = list(self.blanks)
                self.blanks[i] = letter
                self.blanks = ''.join(self.blanks)
