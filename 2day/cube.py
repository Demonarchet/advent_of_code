import numpy as np

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def is_game_possible(line):
    sets = line.split(';')
    for set in sets:
        colors = set.split(',')
        for color in colors:
            color = color.strip()
            value, color = color.split(' ')

            if color == "red":
                if int(value) > MAX_RED:
                    return False
            elif color == "green":
                if int(value) > MAX_GREEN:
                    return False
            elif color == "blue":
                if int(value) > MAX_BLUE:
                    return False
            else:
                return False
    return True

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        total_result = 0

        for i, line in enumerate(lines):
            game_values = line.split(':')[1]
            if is_game_possible(game_values):
                total_result += i + 1
        print(total_result)