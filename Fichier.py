import pickle

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def who_am_i(self):
        print("{} ({})".format(self.name, self.level))

#p1 = Player("Juste", 57)
#p1.who_am_i()

with open("player.data", "rb") as fic:
    get_record = pickle.Unpickler(fic)
    player_one = get_record.load() 

player_one.who_am_i()