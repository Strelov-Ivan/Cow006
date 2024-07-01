from All_classes.Hand_class import Hand
from All_classes.player_class import player, AI, Human
from All_classes.Card_class import Card
import random

def test_create():
    x = sorted(random.sample(range(1, 105), 25))
    b = Hand()
    values = []
    for i in range(5):
        b.add_card(Card(x[i]))
        values.append(x[i])
    p = player(name='Alex', hand=b)
    print(b.cards)
    assert p.name == 'Alex'
    assert p.Hand.cards == values
    assert isinstance(p.actor, AI)

def test_human():
    x = sorted(random.sample(range(1, 105), 25))
    b = Hand()
    values = []
    for i in range(5):
        b.add_card(Card(x[i]))
        values.append(x[i])
    p = player(name='Bob', hand=b, is_human=True)
    print(b.cards)
    assert p.name == 'Bob'
    assert p.Hand.cards == values
    assert isinstance(p.actor, Human)


