from Card_class import Card
class Hand:
    def __init__(self, *args):
        self.cards = []
        for i in args:
            self.cards.append(i.value)

    def __repr__(self):
        cards = []
        for i in self.cards:
            cards.append(i.value)
        return str(cards)
        # return [Card(v) for v in self.cards.value]

    def add_card(self, Card):
        self.cards.append(Card)

    def remove_card(self, Card):
        self.cards.remove(Card)

    def score(self):
        summ = 0
        for i in self.cards:
            summ += i.point
        return summ

    #def save(self):
        #d = dict()
        #for i in self.cards:
            #d[]
