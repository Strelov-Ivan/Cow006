from Field_class import Field
from player_class import player,Human,AI
from Card_class import Card
from Hand_class import Hand
from Gamestate_class import Gamestate
import random

def test_gamestate_creation():
    a = Gamestate([player('Bob', None), player('Alex', None)])
    print(a.Field, a.players[0], a.players[1])
    assert [a.players[i].name for i in range(2)] == ['Bob', 'Alex']
    assert len(a.players[0].Hand.cards) == 10
    assert len(a.players[1].Hand.cards) == 10



