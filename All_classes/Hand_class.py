from Card_class import Card


class Hand:
    def __init__(self, *args):
        self.cards = []
        for i in args:
            self.cards.append(i.value)

    def __repr__(self):
        cards = []
        for i in self.cards:
            cards.append(i)
        return str(cards)
        # return [Card(v) for v in self.cards.value]

    def add_card(self, card):
        self.cards.append(card.value)

    def remove_card(self, card):
        self.cards.remove(card.value)

    def score(self):
        summ = 0
        for i in self.cards:
            summ += Card(i).point
        return summ

    def __len__(self):
        return len(self.cards)





    # def take_cards(self, Player):
    #     values = [x.value for x in self.cards]
    #     a = self.score()
    #     Player.points += a
    #     last_card = values[-1]
    #     self.cards = Card(last_card)
    #     print(f'Six cards in the row #{self.index}! {Player.name} takes {str(values[0:-1])}.')