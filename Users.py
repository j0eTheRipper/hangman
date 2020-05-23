class User:
    def __init__(self, usr_name):
        self.usr_name = usr_name
        # Adding the score variable.
        try:
            self.scores = open('.scores.txt', 'r')
        except FileNotFoundError:
            self.score = 0
            open('.scores.txt', 'w')  # Creates the scores file.
            self.scores = open('.scores.txt', 'r')
        finally:
            if self.usr_name not in self.scores.read():  # If the user is new
                self.score = 0
                # Opens the scores file and adds the user without overwriting the file.
                self.scores = open('.scores.txt', 'a')
                print(self.usr_name, self.score, file=self.scores)
            else:  # If the user is existing
                self.scores.seek(0)
                for name_score in self.scores:
                    name = name_score.split()[0]
                    if name == self.usr_name:
                        self.score = int(name_score.split()[1].replace('\n', ''))
            self.scores.close()

    def score_handler(self, pts):
        """Reads and modifies the scores"""
        scores_read = open('.scores.txt', 'r')
        scores = dict()
        # Adds the users and their scores to the scores dict
        for usr_info in scores_read:
            scores[usr_info.split()[0]] = int(usr_info.split()[1].replace('\n', ''))
        scores_read.close()

        scores[self.usr_name] += pts
        self.score += pts
        scores_write = open('.scores.txt', 'w')
        # Saving the scores to the scores file
        for usr_, pts_ in scores.items():
            print(usr_, pts_, file=scores_write, flush=True)
        scores_write.close()
