from Card_class import Card


class Hand:
    def __init__(self, *args):
        self.cards = []
        for i in args:
            self.cards.append(i)

    def __repr__(self):
        cards = []
        for i in self.cards:
            cards.append(i.value)
        return str(cards)
        # return [Card(v) for v in self.cards.value]

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def score(self):
        summ = 0
        for i in self.cards[:-2]:
            summ += i.point
        return summ



    def take_cards(self, player):
        values = [x.value for x in self.cards]
        a = self.score()
        player.points += a
        last_card = values[-1]
        self.cards = Card(last_card)
        print(f'Six cards in the row #{self.index}! {player.name} takes {str(values[0:-1])}.')