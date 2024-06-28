class Row:
    def __init__(self, *cards):
        self.cards = []
        for i in cards:
            self.cards.append(i)

    def __repr__(self):
        cards = []
        for i in self.cards:
            cards.append(i.value)
        return str(cards)

    def add_card(self, Card):
        self.cards.append(Card)

    def remove_cards(self, Card):
        self.cards.remove(Card)

    def score(self):
        summ = 0
        for i in self.cards:
            summ += i.point
        return summ