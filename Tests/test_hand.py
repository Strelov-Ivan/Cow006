import pytest
import random
from Card_class import Card
from Hand_class import Hand

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
