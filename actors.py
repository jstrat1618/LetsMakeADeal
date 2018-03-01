class Door():
    def __init__(self, id, prize):
        self.id = id
        self.prize = prize

    def __repr__(self):
        return 'Door {} is a {}'.format(self.id, self.prize)


class Player():
    def __init__(self, name, num_wins=0):
        self.name  = name
        self.num_wins = num_wins

    def __repr__(self):
        return "Player {} has won {} games.".format(self.name, self.num_wins)

    def strategy(self, answer):
        self.answer = answer

    def door_choice(self, choice):
        self.choice = choice