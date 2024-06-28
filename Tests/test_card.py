import random
from Classes.Card_class import Card

def test_Card():
    x = random.sample(range(0, 105), 5)
    for i in range(len(x)):
        a = Card(x[i])
        assert a.value == x[i]

