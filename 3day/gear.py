import numpy as np

def check_if_part(lines, lineIdx, nbIdx):
    endIdx = nbIdx

    # Get indexes of the number
    while endIdx < len(lines[lineIdx]) and lines[lineIdx][endIdx].isdigit():
        endIdx += 1
    total_num = lines[lineIdx][nbIdx:endIdx]

    # Check if the character before is a symbol
    if nbIdx > 0 and not lines[lineIdx][nbIdx-1].isalnum() and not lines[lineIdx][nbIdx-1] == '.':
        return True, total_num, endIdx

    # Check if the character after is a symbol
    if endIdx < len(lines[lineIdx]) - 1 and not lines[lineIdx][endIdx].isalnum() and not lines[lineIdx][endIdx] == '.':
        return True, total_num, endIdx

    if nbIdx > 0:
        nbIdx -= 1
    if endIdx < len(lines[lineIdx]):
        endIdx += 1

    # Check if the characters above are a symbol
    if lineIdx > 0:
        for k in range(nbIdx, endIdx):
            if not lines[lineIdx-1][k].isalnum() and not lines[lineIdx-1][k] == '.' and not lines[lineIdx-1][k] == '\n':
                return True, total_num, endIdx
    
    # Check if the characters below are a symbol
    if lineIdx < len(lines) - 1:
        for k in range(nbIdx, endIdx):
            if not lines[lineIdx+1][k].isalnum() and not lines[lineIdx+1][k] == '.' and not lines[lineIdx+1][k] == '\n':
                return True, total_num, endIdx

    return False, total_num, endIdx

if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
        total_result = 0

        for lineIdx in range(len(lines)):
            line = lines[lineIdx]
            nbIdx = 0
            while nbIdx < len(line):
                if line[nbIdx].isdigit():
                    isPart, total_num, endIdx = check_if_part(lines, lineIdx, nbIdx)
                    if isPart:
                        total_result += int(total_num)
                    nbIdx = endIdx - 1
                nbIdx += 1

        print(total_result)