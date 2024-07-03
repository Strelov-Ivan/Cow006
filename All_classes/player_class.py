from Hand_class import Hand
from Card_class import Card
from Field_class import Field
import random
class Human:
    def choose_card(self, hand: Hand) -> int:
        print('Choose a card to play')
        while True:
            try:
                res = int(input())
                # card = Card(res)
                if res in hand.cards:
                    return res
                else:
                    print("You don't have this card. Choose valid card")
            except (ValueError, KeyError, IndexError):
                print("Invalid choosen card. Choose a card in your hand as 1, 56 or 101.")

class AI:
    def choose_card(self, hand: Hand) -> Card:
        cards = [c for c in hand.cards]
        print (cards[0])
        return cards[0] if cards else None
class player:

    def __init__(self, name: str, hand: Hand() = None, is_human: bool=False):
        self.name = name
        self.Hand = hand
        if self.Hand == None:
            self.Hand = Hand()
        self.points = 0
        if is_human:
            self.actor = Human()
        else:
            self.actor = AI()
    def __repr__(self):
        cards = ''
        for i in self.Hand.cards:
            cards += f'{i} '
        return f'{self.name}: {cards}'

    def choose_card(self):
        return self.actor.choose_card(self.Hand)

    def choose_row(self, field: Field, card:Card):
        print('Field:')
        print(field)
        print(f'Played card is too little! {self.name} chooses a row to take as a penalty')
        if isinstance(self.actor, Human):
            while True:
                try:
                    res = int(input())
                    if res < 1 or res > 4:
                        raise ValueError
                    self.points += field.rows[res-1].score()
                    field.rows[res-1].cards = [card.value]
                    print('New field:')
                    print(field)
                    break
                except (ValueError, KeyError, IndexError):
                    print("Invalid choosen row. Choose a row by printing it's index: 1, 2, 3 or 4.")
        else:
            choosen_card = random.randint(1, 4)
            print(choosen_card)
            self.points += field.rows[choosen_card-1].score()
            field.rows[choosen_card - 1].cards = [card.value]
            print('New field:')
            print(field)
def human_choose_card():
    han1 = Hand(Card(1), Card(55), Card(99), Card(101))
    p = player(name='Cow006', hand=han1, is_human=True)
    print(p)
    card = p.choose_card()
    print('Choosen card:', card)

def human_choose_row():
    han1 = Hand(Card(1), Card(54), Card(99), Card(101))
    Row1 = Hand(Card(2), Card(6), Card(8))
    Row2 = Hand(Card(3), Card(7), Card(9))
    Row3 = Hand(Card(4), Card(8), Card(10))
    Row4 = Hand(Card(11), Card(55))

    f = Field([Row1, Row2, Row3, Row4])
    p = player(name='Cow006', hand=han1, is_human=True)
    print('Cow006 points:', p.points)
    p.choose_row(f, Card(1))
    print('Cow006 New Points:', p.points)


if __name__ == '__main__':
    human_choose_card()
    human_choose_row()
