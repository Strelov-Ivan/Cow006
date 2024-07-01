from Hand_class import Hand
from Card_class import Card
class Human:
    def __init__(self):
        pass
class AI:
    def __init__(self):
        pass
class player:
    def __init__(self, name: str, hand: Hand() = None, is_human: bool=False):
        self.name = name
        self.Hand = hand
        self.points = 0
        if is_human:
            self.actor = Human()
        else:
            self.actor = AI()
    def __repr__(self):
        cards = ''
        for i in self.Hand.cards:
            cards += f'{i.value} '
        return f'{self.name}: {cards}'



