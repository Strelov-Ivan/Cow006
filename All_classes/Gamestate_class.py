from Field_class import Field
from player_class import Player, Human, AI
from Card_class import Card
from Hand_class import Hand
import random


class Gamestate:
    CARDS_PER_PLAYER = 10
    def __init__(self, players=list[Player], field=Field(), iplayer: int=0):
        self.players = players
        self.iplayer = iplayer
        self.field = field
        self.deck = random.sample(range(1, 105), len(list(self.players)) * self.CARDS_PER_PLAYER +
                                  self.field.NUMBER_OF_ROWS)

    def play_card_to(self, card: Card, iplayer: int):
        last_cards_values = sorted(list(self.field.last_cards().values()))
        last_cards = self.field.last_cards()
        index = None
        if card.value < last_cards_values[0]:
            self.players[iplayer].choose_row(self.field, card)
        elif card.value < last_cards_values[1]:
            index = list(filter(lambda x: last_cards[x] == last_cards_values[0], last_cards))[0]
        elif card.value < last_cards_values[2]:
            index = list(filter(lambda x: last_cards[x] == last_cards_values[1], last_cards))[0]
        elif card.value < last_cards_values[3]:
            index = list(filter(lambda x: last_cards[x] == last_cards_values[2], last_cards))[0]
        elif card.value > last_cards_values[3]:
            index = list(filter(lambda x: last_cards[x] == last_cards_values[3], last_cards))[0]
        if index is not None:
            self.field.rows[index].add_card(card)
            if len(self.field.rows[index].cards) == 6:
                print('Field:')
                print(self.field)
                print(f"Six cards in the row! {self.players[iplayer].name} takes {self.field.rows[index].cards[0:-1]}.")
                self.players[iplayer].points += self.field.rows[index].score()
                self.players[iplayer].points -= card.point
                self.field.rows[index].cards = []
                self.field.rows[index].add_card(card)

    def new_game(self):
        for i in range(self.field.NUMBER_OF_ROWS):
            self.field.rows[i].add_card(Card(self.deck[-self.field.NUMBER_OF_ROWS+i]))
        n = 0
        for p in self.players:
            cards = [Card(self.deck[i+n*self.CARDS_PER_PLAYER]) for i in range(self.CARDS_PER_PLAYER)]
            for c in cards:
                p.hand.add_card(c)
            n += 1
        self.field = Field([Hand(Card(self.deck[i])) for i in range(-self.field.NUMBER_OF_ROWS, 0)])