class Door():
    def __init__(self, id, prize):
        self.id = id
        self.prize = prize

    def __repr__(self):
        return 'Door {} is a {}'.format(self.id, self.prize)