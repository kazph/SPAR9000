import random as rand
import itertools

# 0000 0000
#  ttt nnnn

# Creating a card e.g. new_card = SPADES + 13 -> Spades King!

SPADES = 0b0100_0000 # = 64
CLUBS  = 0b0101_0000 # = 80
JECK   = 0b0110_0000 # = 96
HEARTS = 0b0111_0000 # = 112

# Clubs at the end, so it gets cut-off during shuffeling
types = [ SPADES, JECK, HEARTS, CLUBS ]
cards = [ type + number for type in types for number in range(2, 15) ]

def get_type(card):
    return card & 0b0111_0000

def get_number(card):
    return card & 0b0000_1111

class QueenOfSpades:
    players: int = 4
    stacks: list[list[int]] = []
    holding_cards: list[list[int]] = []
    previus_round_winner = 0

    def get_played_cards(self) -> list[int]:
        return set(flatten(self.stacks))
    
    def __init__(self, players = 4, seed = None) -> None:
        self.players = players
        self.stacks = [[] for _ in range(players)]
        self.holding_cards = [[] for _ in range(players)]

        shuffled_cards = cards[:-( 52 % players)] if 52 % players > 0 else cards

        if seed != None:
            rand.seed = seed
        rand.shuffle(shuffled_cards)

        for idx, card in enumerate(shuffled_cards):
            self.holding_cards[idx % players].append(card)

    def play(self):
        for round in range(0, 52 // self.players):
            print(f"Round {round} - {self.previus_round_winner} starts")
            played_cards = []

            for player in range(self.previus_round_winner, self.previus_round_winner + self.players):
                player = player % self.players
                print(f"Player {player} played XX")
            
            self.previus_round_winner = rand.randint(0, self.players - 1)
            print(f"Player {self.previus_round_winner} won")

game = QueenOfSpades(players=5)
game.play()


def player_play(holding_cards: list[int], round_cards: list[int], players_left = int):
    return rand.choice(holding_cards)