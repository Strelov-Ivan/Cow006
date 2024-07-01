from Card_class import Card
from Hand_class import Hand
#from player_class import player

class Field:
    def __init__(self, Row1, Row2, Row3, Row4):
        self.index0 = Row1
        self.index1 = Row2
        self.index2 = Row3
        self.index3 = Row4

    def __repr__(self):
        return (f'{str(self.index0)} \n'
                f'{str(self.index1)} \n'
                f'{str(self.index2)} \n'
                f'{str(self.index3)} \n')

    def last_cards(self):
        return {'0': self.index0.cards[-1], '1': self.index1.cards[-1],'2': self.index2.cards[-1],'3': self.index3.cards[-1],}
