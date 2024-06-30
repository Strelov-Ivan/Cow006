from Card_class import Card


class Row:
    def __init__(self, index, *cards):
        self.index = index
        self.cards = []
        for i in cards:
            self.cards.append(i)

    def __repr__(self):
        cards = []
        for i in self.cards:
            cards.append(i.value)
        return str(cards)

    def add_card(self, card):
        self.cards.append(card)

    def remove_cards(self, card):
        self.cards.remove(card)

    def score(self):
        summ = 0
        for i in self.cards:
            summ += i.point
        return summ




