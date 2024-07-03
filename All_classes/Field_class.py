from Card_class import Card
from Hand_class import Hand
#from player_class import player

class Field:
    def __init__(self, rows = None):
        if rows is None:
            rows = [Hand(),Hand(),Hand(),Hand()]
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


        # return (str1 + '\n' + str2 + '\n' + str3 + '\n' + str4)


    def last_cards(self):
        return [{i: row[-1] for i, row in enumerate(self.rows)}]
