import numpy as np


def count_winning_numbers(card_winning, card_owned):
    result = 0
    for val in card_winning:
        if val.isdigit():
            if val in card_owned:
                if result == 0:
                    result = 1
                else:
                    result *= 2
    return result

def get_cards_info(card):
    card = card.replace('\n', '')
    card = card.split(':')
    card_nb = card[0].split(' ')[1]
    card_infos = card[1].split('|')
    card_winning = card_infos[0].split(' ')
    card_owned = card_infos[1].split(' ')
    return card_winning, card_owned

if __name__ == '__main__':
    with open('input.txt') as f:
        cards = f.readlines()
        total_result = 0
        for card in cards:
            card_winning, card_owned = get_cards_info(card)
            value = count_winning_numbers(card_winning, card_owned)
            total_result += value
        
        print(total_result)