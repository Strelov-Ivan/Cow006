from Field_class import Field
from player_class import Player, Human, AI
from Card_class import Card
from Hand_class import Hand
from Gamestate_class import Gamestate
import random

# def test_gamestate_creation():
#     a = Gamestate([Player('Bob', None), Player('Alex', None)])
#     print(a.field, a.players[0], a.players[1])
#     assert [a.players[i].name for i in range(2)] == ['Bob', 'Alex']
#     assert len(a.players[0].hand.cards) == 10
#     assert len(a.players[1].hand.cards) == 10

def test_new_game():
    a = Gamestate([Player('Bob', None), Player('Alex', None)])
    a.new_game()
    print(a.field)
    print(a.players[0])
    print(a.players[1])
    assert len(a.players[0].hand.cards) == 10
    assert len(a.players[1].hand.cards) == 10
