from random import shuffle as rshuffle

from .card import Card


class Deck:
    """
    Class representing a deck. The first time we create, we seed the static 
    deck with the list of unique card integers. Each object instantiated simply
    makes a copy of this object and shuffles it. 
    """
    _FULL_DECK: list[int] = []

    def __init__(self) -> None:
        self.shuffle()

    def __iter__(self):
        return self.cards.__iter__()

    # def __next__(self):
    #     return self.cards.__next__()

    def shuffle(self) -> None:
        # and then shuffle
        self.cards = Deck.GetFullDeck()
        rshuffle(self.cards)

    def draw(self, n: int = 1) -> list[int]:
        cards = []
        for _ in range(n):
            cards.append(self.cards.pop())
        return cards

    def deleteCards(self, cards: list[int]):
        for ele in cards:
            self.cards.remove(ele)

    def __str__(self) -> str:
        return Card.ints_to_pretty_str(self.cards)

    @staticmethod
    def GetFullDeck() -> list[int]:
        if Deck._FULL_DECK:
            return list(Deck._FULL_DECK)

        # create the standard 52 card deck
        for rank in Card.STR_RANKS:
            for suit, _ in Card.CHAR_SUIT_TO_INT_SUIT.items():
                Deck._FULL_DECK.append(Card.new(rank + suit))

        return list(Deck._FULL_DECK)