from Card_class import Card
from Hand_class import Hand
#from player_class import player
import random
import pytest

# def test_Card():
#     x = random.randint(0, 104)
#     a = Card(x)
#     assert a.value == x

def RanCards(numbers):
    for i in range(len(numbers)):
        a = Card(numbers[i])
        print (f'{numbers[i]}:{a.point}')

x = random.sample(range(0, 105), 5)
RanCards(x)
Hand1 = Hand()
for i in range(len(x)):
    a = Card(x[i])
    Hand1.add_card(a)
print(Hand1)

