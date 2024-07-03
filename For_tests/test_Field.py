import random

from All_classes.Card_class import Card
from All_classes.Hand_class import Hand
from All_classes.player_class import player
from All_classes.Field_class import Field

def test_Field_last_cards_def():
    Rows = []
    values = [1, 4, 35, 56, 32, 46, 74, 102, 3, 67, 89, 91, 13, 17, 21, 79]
    for x in range(4):
        hand = Hand()
        for i in range(4):
            a = Card(values[i+4*x])
            hand.add_card(a)
        Rows.append(hand)
    f = Field(Rows)
    print(f.last_cards().values())
    assert f.last_cards() == {0:56, 1:102, 2:91, 3:79}
