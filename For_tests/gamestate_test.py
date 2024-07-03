from Field_class import Field
from player_class import player,Human,AI
from Card_class import Card
from Hand_class import Hand
from Gamestate_class import Gamestate
import random

def gamestate_test():
    Rows = []
    values = [1, 4, 35, 56, 32, 46, 74, 102, 3, 67, 89, 91, 13, 17, 21, 79]
    for x in range(4):
        hand = Hand()
        for i in range(4):
            a = Card(values[i + 4 * x])
            hand.add_card(a)
        Rows.append(hand)
    f = Field(Rows)
    a = Gamestate([player('Bob', Hand(Card(6), Card(8))), player('Alex', Hand(Card(90), Card(55)), True)], f)
    print(a.Field, a.players[1])
    print("Points:", a.players[1].points)
    choosen_card = Card(a.players[1].choose_card())
    Row = a.play_card_to(choosen_card, iplayer=1)
    print(a.Field)
    print("Alex's new points:", a.players[1].points)

def gamestate_test2():
    Rows = []
    values = [1, 4, 35, 56, 32, 46, 74, 102, 3, 67, 89, 91, 13, 17, 21, 79]
    for x in range(4):
        hand = Hand()
        for i in range(4):
            a = Card(values[i + 4 * x])
            hand.add_card(a)
        Rows.append(hand)
    f = Field(Rows)
    f.rows[0].add_card(Card(54))
    a = Gamestate([player('Bob', Hand(Card(6), Card(8))), player('Alex', Hand(Card(90), Card(55)), True)], f)
    print(a.Field, a.players[1])
    print("Points:", a.players[1].points)
    choosen_card = Card(a.players[1].choose_card())
    Row = a.play_card_to(choosen_card, iplayer=1)
    print(a.Field)
    print("Alex's new points:", a.players[1].points)
if __name__ == '__main__':
    gamestate_test2()