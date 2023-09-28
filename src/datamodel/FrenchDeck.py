
import collections

from random import choice
Card = collections.namedtuple('Card' , ['rank' , 'suit'])


suit_values = dict(spades=3 , hearts=2 , diamonds=1 , clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
class FrenchDeck:

    ranks = [str(x) for x in range(2 , 11)] + list('JQKA')
    suites = 'spades diamonds clubs hearts'.split()


    def __init__(self):
        self._cards = [Card(rank , suit) for suit in self.suites
                                       for rank in self.ranks ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


if __name__ == "__main__":
    deck = FrenchDeck()
    card = deck[0]
    print(card)
    card = deck[-1]
    print(card)
    card = choice(deck)
    print(card)

    print(deck[:3])
    print(deck[-3:])


    for card in deck:
        print(card)

    for card in reversed(deck):
        print(card)


    print(Card('Q' , 'hearts') in deck)

    for card in sorted(deck ,key=spades_high):
        print(card)

