class player:
    def __init__(self, name, Hand):
        self.name = name
        self.Hand = Hand
        self.points = 0
    def __repr__(self):
        cards = ''
        for i in self.Hand.cards:
            cards += f'{i.value} '
        return f'{self.name}: {cards}'



