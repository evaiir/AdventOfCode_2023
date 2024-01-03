from functools import cmp_to_key
from typing import Counter
hands = {}
bids = open("inpt.txt").read().splitlines()
for entry in bids:
    hand, bid = entry.split()
    hands[hand] = int(bid)

card_rank = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

def isFiveKind(hand):
    return hand.count(hand[0]) == 5


def isFourKind(hand):
    return hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4


def isFullHouse(hand):
    return set(Counter(hand).values()) == {2, 3}


def isThreeKind(hand):
    return set(Counter(hand).values()) == {1, 3}


def isTwoPair(hand):
    return set(Counter(hand).values()) == {1, 2} and len(set(hand)) == 3


def isOnePair(hand):
    return set(Counter(hand).values()) == {1, 2} and len(set(hand)) == 4


def isHighCard(hand):
    return len(set(hand)) == 5


def getHandValue(hand):
    check_type = [
        isHighCard,
        isOnePair,
        isTwoPair,
        isThreeKind,
        isFullHouse,
        isFourKind,
        isFiveKind,
    ]
    for c in range(len(check_type)):
        if check_type[c](hand):
            return c

ranked_hands = {}
for hand in hands:
    ranked_hands[hand] = getHandValue(hand)

ordered_hands = []
for hand in hands:
    full_info = []
    full_info.append(hand)
    full_info.append(hands[hand])
    full_info.append(ranked_hands[hand])
    ordered_hands.append(full_info)

def comp(h1, h2):
    if h1[2] > h2[2]:
        return 1
    if h2[2] > h1[2]:
        return -1
    for c1, c2 in zip(h1[0], h2[0]):
        if card_rank[c1] > card_rank[c2]:
            return 1
        if card_rank[c2] > card_rank[c1]:
            return -1

    return 0

ordered_hands.sort(key=cmp_to_key(comp))
sum = 0
for i in range(len(ordered_hands)):
    sum += ordered_hands[i][1] * (i + 1)

print(sum)
