import numpy as np

copy = {}

def add_in_copy(card, number):
    if card in copy:
        copy[card] += number
    else:
        copy[card] = number

def count_winning_numbers(card_nb, card_winning, card_owned):
    add_in_copy(card_nb, 1)
    result = 1
    for val in card_winning:
        if val.isdigit():
            if val in card_owned:
                result += 1
    
    int_card_nb = int(card_nb)
    for i in range(1, result):
        add_in_copy(str(int_card_nb + i), copy[card_nb])

    return result

def get_cards_info(card):
    card = card.replace('\n', '')
    card = card.split(':')
    card_nb = card[0].split(' ')[-1]
    card_infos = card[1].split('|')
    card_winning = card_infos[0].split(' ')
    card_owned = card_infos[1].split(' ')
    return card_nb, card_winning, card_owned

if __name__ == '__main__':
    with open('input.txt') as f:
        cards = f.readlines()
        total_result = 0
        for card in cards:
            card_nb, card_winning, card_owned = get_cards_info(card)
            count_winning_numbers(card_nb, card_winning, card_owned)

        for key in copy:
            total_result += copy[key]

        print(total_result)