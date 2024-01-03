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
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}

def isFiveKind(hand, joker_count, non_joker_cards):
    if joker_count == 5:
        return True
    card_count = set(Counter(non_joker_cards).values())
    return any(count + joker_count == 5 for count in card_count)

def isFourKind(hand, joker_count, non_joker_cards):
    if joker_count == 0:
        return hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4
    card_count = set(Counter(non_joker_cards).values())
    return any(count + joker_count == 4 for count in card_count)

def isFullHouse(hand, joker_count, non_joker_cards):
    if joker_count == 0:
        return set(Counter(hand).values()) == {2, 3}
    if joker_count > 1:
        return False
    if len(Counter(non_joker_cards)) == 2:
        return True
    
    return False

def isThreeKind(hand, joker_count, non_joker_cards):
    if joker_count == 0:
        return set(Counter(hand).values()) == {1, 3}
    if joker_count > 2:
        return False
    if len(Counter(non_joker_cards)) == 3:
        return True
    
    return False

def isTwoPair(hand, joker_count, non_joker_cards):
    if joker_count == 0:
        return set(Counter(hand).values()) == {1, 2} and len(set(hand)) == 3
    if joker_count > 1:
        return False
    if len(Counter(non_joker_cards)) == 2:
        return True
    
    return False

def isOnePair(hand, joker_count, non_joker_cards):
    if joker_count == 0:
        return set(Counter(hand).values()) == {1, 2} and len(set(hand)) == 4
    if joker_count == 1:
        if len(Counter(non_joker_cards)) == 4:
            return True
    return False

def isHighCard(hand, joker_count, non_joker_cards):
    return len(Counter(non_joker_cards)) == 5

def getHandValue(hand):
    joker_count = hand.count("J")
    non_joker_cards = [card for card in hand if card != "J"]
    for c in range(len(check_type)):
        if check_type[c](hand, joker_count, non_joker_cards):
            return c

check_type = [
    isFiveKind,
    isFourKind,
    isFullHouse,
    isThreeKind,
    isTwoPair,
    isOnePair,
    isHighCard,
]

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
            return -1
        if card_rank[c2] > card_rank[c1]:
            return 1

    return 0


ordered_hands.sort(key=cmp_to_key(comp))
sum = 0
for i in range(len(ordered_hands)):
    ordered_hands[i][2] = (len(ordered_hands) - i)
    sum += ordered_hands[i][2] * ordered_hands[i][1]

print(sum)
