import random

from All_classes.Card_class import Card
from All_classes.Hand_class import Hand


def test_Hand():
    x = random.sample(range(0, 105), 5)
    b = Hand()
    values = []
    for i in range(len(x)):
        a = Card(x[i])
        b.add_card(a)
        values.append(x[i])
    a = b.__repr__()
    assert a == str(values)
    #assert b.score() in range (0, 105)


def test_Hand_score():
    x = random.sample(range(0, 105), 5)
    b = Hand()
    points = 0
    for i in range(len(x)):
        a = Card(x[i])
        b.add_card(a)
        points += a.point
    a = b.score()
    assert a == points
