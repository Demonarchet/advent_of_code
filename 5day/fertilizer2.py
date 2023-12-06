import numpy as np

def get_range(start, nb):
    int_start = int(start)
    nb = int(nb)
    
    # r = np.arange(start, start + nb)
    # r = np.char.mod('%d', r)
    r = (start, str(int_start + nb))
    return r

def get_all_ranges(ranges):
    values = []
    i = 0
    while i < len(ranges):
        values.append(get_range(ranges[i], ranges[i+1]))
        i += 2
    return values

def concatenate_ranges(ranges):
    ranges.sort()
    concatenated = [ranges[0]]
    for start, end in ranges[1:]:
        last_start, last_end = concatenated[-1]
        if start <= last_end:
            concatenated[-1] = (last_start, max(last_end, end))
        else:
            concatenated.append((start, end))
    return concatenated

# def get_all_values(ranges):
#     values = []
#     for range in ranges:
#         print(range)
#         r = np.arange(int(range[0]), int(range[1]))
#         r = np.char.mod('%d', r)
#         values.append(r)
#     return values

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
        ranges = seeds(lines[0])
        ranges = get_all_ranges(ranges)
        values = concatenate_ranges(ranges)
        # values = get_all_values(values)

        print(values)

        # updated = [False] * len(values)

        # for line in lines[1:]:
        #     nb_elem = len(line.split())
        #     if nb_elem != 3:
        #         updated = [False] * len(values)
        #         continue
        #     for idx, v in enumerate(values):
        #         if updated[idx]:
        #             continue
        #         values[idx], updated[idx] = get_new_value(v, line)
    
        # values = np.array(values, dtype=np.int64)
        # print(np.min(values))