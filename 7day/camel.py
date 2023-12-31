import numpy as np

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'T', 'J','Q', 'K', 'A']
types = ["nothing", "pair", "2pair", "three", "full", "four", "five"]

hands = []
ranks = []

def count_pair(hand):
    count = 0
    for card in hand:
        if hand[card] == 2:
            count += 1
    return count

def check_five(hand):
    if len(hand) == 1:
        return 1
    return 0

def check_four(hand):
    if len(hand) != 2:
        return 0
    for card in hand:
        if hand[card] == 4:
            return 1
    return 0

def check_full(hand):
    if len(hand) != 2:
        return 0
    nb = 5
    for card in hand:
        nb -= hand[card]
        if nb == 2 or nb == 3:
            return 1
    return 0

def check_three(hand):
    if len(hand) != 3:
        return 0
    for card in hand:
        if hand[card] == 3:
            return 1
    return 0

def add_cart_in_hand(cards):
    hand = {}
    for card in cards:
        if card in hand:
            hand[card] += 1
        else:
            hand[card] = 1
    return hand

def get_type(hand):
    if check_five(hand):
        return "five"
    if check_four(hand):
        return "four"
    if check_full(hand):
        return "full"
    if check_three(hand):
        return "three"
    if count_pair(hand) == 2:
        return "2pair"
    if count_pair(hand) == 1:
        return "pair"
    return "nothing"

def check_hand_value(hand):
    pw = 12
    value = 0
    for card in hand:
        value += 10**pw * cards.index(card)
        pw -= 2
    return value
    

def give_final_rank(ranks, hands):
    final_rank = []
    r = 1
    for t in types:
        rank_indexes = []
        for i in range(len(ranks)):
            if ranks[i] == t:
                rank_indexes.append(i)
        rank_indexes.sort(key=lambda x: check_hand_value(hands[x][0]))
        final_rank += rank_indexes
    return final_rank

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            hd = line[0]
            bid = line[1]
            hand = add_cart_in_hand(hd)
            hands.append((hd, hand, bid))
        for hand in hands:
            ranks.append(get_type(hand[1]))
        ranks = give_final_rank(ranks, hands)
        result = 0
        for i in range(len(ranks)):
            result += (i+1) * int(hands[ranks[i]][2])
        print(result)