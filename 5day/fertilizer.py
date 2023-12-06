import numpy as np

def seeds(line):
    return line.split(":")[1].split()

def get_new_value(value, line):
    int_value = int(value)
    l = line.split()
    new_start = int(l[0])
    old_start = int(l[1])
    end = int(l[2])

    if new_start == old_start:
        return value, True
    
    if int_value >= old_start and int_value < old_start + end:
        return str(new_start + (int_value - old_start)), True

    return value, False

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        values = seeds(lines[0])

        updated = [False] * len(values)

        for line in lines[1:]:
            nb_elem = len(line.split())
            if nb_elem != 3:
                updated = [False] * len(values)
                continue
            for idx, v in enumerate(values):
                if updated[idx]:
                    continue
                values[idx], updated[idx] = get_new_value(v, line)
    
        values = np.array(values, dtype=np.int64)
        print(np.min(values))