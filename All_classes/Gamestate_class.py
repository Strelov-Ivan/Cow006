from Field_class import Field
from player_class import player,Human,AI
from Card_class import Card
from Hand_class import Hand
import random


class Gamestate:
    def __init__(self, players=list[player], field=Field(), iplayer: int=0):
        self.players = players
        self.iplayer = iplayer
        self.Field = field
        if len(self.players[0].Hand.cards) == 0:
            x = random.sample(range(0, 105), len(self.players) * 10 + 4)
            for p in self.players:
                cards = [Card(x[i]) for i in range(10)]
                for c in cards:
                    p.Hand.add_card(c)
            self.Field = Field([Hand(Card(x[i])) for i in [-4, -3, -2, -1]])

    def play_card_to(self, card: Card, iplayer: int):
        last_cards_values = sorted(list(self.Field.last_cards().values()))
        last_cards = self.Field.last_cards()
        index = 0
        if card.value < last_cards_values[0]:
            self.players[iplayer].choose_row(self.Field, card)
        elif card.value < last_cards_values[1]:
            index = list(filter(lambda x: last_cards[x] == last_cards_values[0], last_cards))[0]
        elif card.value < last_cards_values[2]:
            index = list(filter(lambda x: last_cards[x] == last_cards_values[1], last_cards))[0]
        elif card.value < last_cards_values[3]:
            index = list(filter(lambda x: last_cards[x] == last_cards_values[2], last_cards))[0]
        elif card.value > last_cards_values[3]:
            index = list(filter(lambda x: last_cards[x] == last_cards_values[3], last_cards))[0]
        self.Field.rows[index].add_card(card)
        if len(self.Field.rows[index].cards) == 6:
            self.players[iplayer].points += self.Field.rows[index].score()
            self.players[iplayer].points -= card.point
            self.Field.rows[index].cards = []
            self.Field.rows[index].add_card(card)
