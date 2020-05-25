class User:
    def __init__(self, usr_name):
        self.usr_name = usr_name
        # Adding the score variable.
        try:
            open('.scores.txt').close()
        except FileNotFoundError:
            self.score = 0
            open('.scores.txt', 'w').close()  # Creates the scores file.
        finally:
            with open('.scores.txt') as scores_r, open('.scores.txt', 'a') as scores_w:
                if self.usr_name not in scores_r.read():  # If the user is new
                    self.score = 0
                    # Opens the scores file and adds the user without overwriting the file.
                    print(self.usr_name, self.score, file=scores_w)
                else:  # If the user is existing
                    scores_r.seek(0)
                    for name_score in scores_r:
                        name = name_score.split()[0]
                        if name == self.usr_name:
                            self.score = int(name_score.split()[1].replace('\n', ''))

    def score_handler(self, pts):
        """Reads and modifies the scores"""
        with open('.scores.txt') as scores_read:
            scores = dict()
            # Adds the users and their scores to the scores dict
            for usr_info in scores_read:
                scores[usr_info.split()[0]] = int(usr_info.split()[1].replace('\n', ''))

        scores[self.usr_name] += pts
        self.score += pts

        with open('.scores.txt', 'w') as scores_write:
            # Saving the scores to the scores file
            for usr_, pts_ in scores.items():
                print(usr_, pts_, file=scores_write, flush=True)
