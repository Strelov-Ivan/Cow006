from Card_class import Card
from Hand_class import Hand
#from player_class import Player

class Field:
    NUMBER_OF_ROWS = 4
    def __init__(self, rows = None):
        if rows is None:
            self.rows = [Hand() for _ in range(self.NUMBER_OF_ROWS)]
        else:
            self.rows = []
            for i in rows:
                self.rows.append(i)

    def __repr__(self):
        all_cards = str()
        for i in self.rows:
            cards = ''.join([f'{x:3}' + ' ' for x in i.cards])
            all_cards += cards
            all_cards += '\n'
        return all_cards


    def last_cards(self):
       return {i: row.cards[-1] for i, row in enumerate(self.rows)}



