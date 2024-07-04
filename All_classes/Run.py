from Field_class import Field
from player_class import Player,Human,AI
from Card_class import Card
from Hand_class import Hand
from Gamestate_class import Gamestate
import random


def run(save_file=None):
    players = []
    if save_file is None:
        print('Choose a player names and decide, which of them will be bots.' +
              " For example, print 'Bob True', after you're done, print anything else.")
        players = []
        while len(players) < 10:
            try:
                name, is_human = map(str, input().split())
                if is_human.lower() in ['true', 'yes', 'yeah', '1']:
                    s = True
                else:
                    s = False
                p = Player(name, None, is_human=s)
                players.append(p)
            except Exception:
                break
    gm = Gamestate(players)
    gm.new_game()
    iplayer = 0
    while len(gm.players[iplayer].hand) > 0:
        cards_played = {}
        for p in gm.players:
            print(f"It's Round {11 - len(p.hand)}, {p.name}!")
            print("Field:")
            print(gm.field)
            print(p)
            print("Your Points:", p.points)
            choosen_card = p.choose_card()
            p.hand.remove_card(Card(choosen_card))
            cards_played[f'{iplayer}'] = choosen_card
            iplayer += 1
            iplayer %= len(gm.players)
            print('----')
        cards_played = sorted(cards_played.items(), key=lambda x: x[1])
        print(f'End of Round{10 - len(p.hand)}')
        for cplayer, card in cards_played:
            print(f'{gm.players[int(cplayer)].name} played {card}')
        for cplayer, card in cards_played:
            gm.play_card_to(Card(card), int(cplayer))
        print('Field after this Round:')
        print(gm.field)
        print('----')
    for p in gm.players:
        print(f"{p.name}'s points:", p.points)



if __name__ == "__main__":
    run()