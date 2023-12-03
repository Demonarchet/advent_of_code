import numpy as np

gears = {}


def add_gear(pos, total_num):
    if pos in gears:
        gears[pos] += [total_num]
    else:
        gears[pos] = [total_num]


def get_gear_index(lines, lineIdx, colIdx):
    return lineIdx * len(lines[0]) + colIdx


def check_if_part(lines, lineIdx, nbIdx):
    endIdx = nbIdx
    while endIdx < len(lines[lineIdx]) and lines[lineIdx][endIdx].isdigit():
        endIdx += 1
    total_num = lines[lineIdx][nbIdx:endIdx]

    if nbIdx > 0 and lines[lineIdx][nbIdx-1] == '*':
        pos = get_gear_index(lines, lineIdx, nbIdx-1)
        add_gear(str(pos), total_num)

    if endIdx < len(lines[lineIdx]) - 1 and lines[lineIdx][endIdx] == '*':
        pos = get_gear_index(lines, lineIdx, endIdx)
        add_gear(str(pos), total_num)

    if nbIdx > 0:
        nbIdx -= 1
    if endIdx < len(lines[lineIdx]):
        endIdx += 1

    if lineIdx > 0:
        for k in range(nbIdx, endIdx):
            if lines[lineIdx-1][k] == '*':
                pos = get_gear_index(lines, lineIdx-1, k)
                add_gear(str(pos), total_num)
    
    if lineIdx < len(lines) - 1:
        for k in range(nbIdx, endIdx):
            if lines[lineIdx+1][k] == '*':
                pos = get_gear_index(lines, lineIdx+1, k)
                add_gear(str(pos), total_num)

    return endIdx

if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
        total_result = 0

        for lineIdx in range(len(lines)):
            line = lines[lineIdx]
            nbIdx = 0
            while nbIdx < len(line):
                if line[nbIdx].isdigit():
                    endIdx = check_if_part(lines, lineIdx, nbIdx)
                    nbIdx = endIdx - 1
                nbIdx += 1

        for key in gears:
            if len(gears[key]) == 2:
                total_result += np.prod(np.array(gears[key]).astype(int))

        print(total_result)