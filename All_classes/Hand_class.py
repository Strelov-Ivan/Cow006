from Card_class import Card


class Hand:
    def __init__(self, *args):
        self.cards = []
        for i in args:
            self.cards.append(i.value)

    def __str__(self):
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

    def six_cards(self, card, player):
        a = self.score()
        player.points += a
        self.cards = [card]





    # def take_cards(self, player):
    #     values = [x.value for x in self.cards]
    #     a = self.score()
    #     player.points += a
    #     last_card = values[-1]
    #     self.cards = Card(last_card)
    #     print(f'Six cards in the row #{self.index}! {player.name} takes {str(values[0:-1])}.')