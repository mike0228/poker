from itertools import combinations

from calcWinner import calcWinner
from treys.deck import Deck


def fun(f, a, b, c, d, comb):
    print(comb[a].__str__() + ',' + comb[b].__str__() + ',' + comb[c].__str__() + ',' + comb[d].__str__(), file=f)
    result = calcWinner([[comb[a], comb[b]], [comb[c], comb[d]]])
    print((result[0] / result[2]).__str__() + "," + (result[1] / result[2]).__str__(), file=f)


f = open("allCombs.txt", "w+")
deck = Deck()
i = 0
for comb in combinations(deck, 4):
    fun(f, 0, 1, 2, 3, comb)
    fun(f, 0, 2, 1, 3, comb)
    fun(f, 0, 3, 1, 2, comb)
    print(i)
    i += 1
