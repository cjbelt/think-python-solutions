"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck, Card


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        self.ranks = {}

        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    # def has_same_suits(self, card_set):
    #     self.suit_hist()

    #     for suit in self.suits.keys():
    #         count = 0

    #         for rank in card_set:
    #             if suit not in self.ranks[rank]:
    #                 break

    #             count += 1

    #             if count == len(card_set):
    #                 print("has same suits")
    #                 return True

    #     print("Not have same suits")
    #     return False

    def has_pair(self):
        self.rank_hist()

        for rank in self.ranks.values():
            if rank == 2:
                return True

        return False

    def has_two_pair(self):
        self.rank_hist()
        count = 0

        for rank in self.ranks.values():
            if rank == 2:
                count += 1

        if count == 2:
            return True

        return False

    def has_three_of_kind(self):
        self.rank_hist()

        for rank in self.ranks.values():
            if rank == 3:
                return True

        return False

    def sorted_cards_rank(self):
        t = []

        for card in self.cards:
            t_card = (card.rank, card.suit, card)
            t.append(t_card)

        t.sort()
        res = []

        for rank, suit, card in t:
            res.append(card)

        return res

    def has_straight(self, n=5):
        self.rank_hist()
        count = 0
        last_rank = 0
        self.ranks[14] = self.ranks.get(1, 0)
        sort_cards = list(self.ranks.items())
        sort_cards.sort()

        for rank, value in sort_cards:
            if (rank == last_rank + 1 or last_rank == 0) and value > 0:
                count += 1
                last_rank = rank
            elif rank == last_rank:
                continue
            else:
                count = 1
                last_rank = rank

            if count == n:
                return True

        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_full_house(self):
        self.rank_hist()
        values = self.ranks.values()

        return 2 in values and 3 in values

    def has_four_of_kind(self):
        self.rank_hist()

        for rank in self.ranks.values():
            if rank >= 4:
                return True

        return False

    def has_straight_flush(self):
        d = {}
        for card in self.cards:
            d.setdefault(card.suit, PokerHand()).add_card(card)

        for hand in d.values():
            if hand.has_straight():
                return True

        return False

    def classify(self):
        self.label = []

        if self.has_straight_flush():
            self.label.append("straight flush")
        if self.has_four_of_kind():
            self.label.append("four of a kind")
        if self.has_full_house():
            self.label.append("full house")
        if self.has_flush():
            self.label.append("flush")
        if self.has_straight():
            self.label.append("straight")
        if self.has_three_of_kind():
            self.label.append("three of a kind")
        if self.has_two_pair():
            self.label.append("two pair")
        if self.has_pair():
            self.label.append("pair")

        # return best combination
        return self.label

class PokerDeck(Deck):
    def deal_hands(self, n_hands=7, n_cards=7):
        t = []

        for i in range(n_hands):
            hand = PokerHand()
            self.move_cards(hand, n_cards)
            t.append(hand)

        return t

def deal_probabilities(h):
    deck = PokerDeck()
    deck.shuffle()

    for hand in deck.deal_hands():
        hand.classify()

        for cl in hand.label:
            h[cl] = h.get(cl, 0) + 1

def print_probabilities(h, n):
    total = 7 * n
    print("Classification \t Probability")

    for cl in h:
        print(cl, "\t", h[cl]/total * 100, "%")


if __name__ == '__main__':
    # make a deck
    # deck = Deck()
    # deck.shuffle()

    # deal the cards and classify the hands
    # for i in range(7):
    #     hand = PokerHand()
    #     deck.move_cards(hand, 7)
    #     hand.sort()
    #     print(hand)
    #     print(hand.classify())
    #     print('')

    # c1 = Card(0, 10)
    # c2 = Card(0, 11)
    # c3 = Card(0, 12)
    # c4 = Card(0, 13)
    # c5 = Card(0, 1)
    # c6 = Card(0, 2)
    # c7 = Card(0, 3)

    # hand = PokerHand()
    # hand.add_card(c1)
    # hand.add_card(c2)
    # hand.add_card(c3)
    # hand.add_card(c4)
    # hand.add_card(c5)
    # hand.add_card(c6)
    # hand.add_card(c7)

    # for card in hand.cards:
    #     print(card.rank, card.suit)

    # print(hand.classify())

    # t1 = ("foo", )
    # print(t1[-1])
    # t2 = ("bar", )
    # t1 += t2
    # print(t1)

    h = {}

    for i in range(100000):
        deal_probabilities(h)

    print_probabilities(h, 100000)
