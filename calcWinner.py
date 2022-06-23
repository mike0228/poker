from itertools import combinations


from treys.deck import Deck
from treys.evaluator import Evaluator


def genAllBoards(hands: list[list[int]]):
    deck = Deck()
    for hand in hands:
        deck.deleteCards(hand)
    boards = []
    for combs in combinations(deck, 5):
        boards.append(list(combs))
    return boards


def calcWinner(hands: list[list[int]]):
    evaluator = Evaluator()
    boards = genAllBoards(hands)
    p1cnt = 0
    p2cnt = 0
    for board in boards:
        best_rank = 7463  # rank one worse than worst hand
        winners = []
        for player, hand in enumerate(hands):
            # evaluate current board position
            rank = evaluator.evaluate(hand, board)
            # detect winner
            if rank == best_rank:
                winners.append(player)
                best_rank = rank
            elif rank < best_rank:
                winners = [player]
                best_rank = rank
        if len(winners) == 1:
            if winners.pop() == 0:
                p1cnt += 1
            else:
                p2cnt += 1
    return [p1cnt, p2cnt, len(boards)]
