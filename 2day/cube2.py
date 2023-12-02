import numpy as np

def get_game_value(line):
    sets = line.split(';')
    red_values = []
    green_values = []
    blue_values = []
    for set in sets:
        colors = set.split(',')
        for color in colors:
            color = color.strip()
            value, color = color.split(' ')
            if color == "red":
                red_values.append(int(value))
            elif color == "green":
                green_values.append(int(value))
            elif color == "blue":
                blue_values.append(int(value))
        
    return np.max(red_values) * np.max(green_values) * np.max(blue_values)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        total_result = 0

        for i, line in enumerate(lines):
            game_values = line.split(':')[1]
            result = get_game_value(game_values)
            total_result += result
        print(total_result)