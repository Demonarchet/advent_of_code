import numpy as np

if __name__ == "__main__":
    values = []

    with open("input.txt", 'r') as f:
        lines = f.readlines()
        speeds = lines[0].split()[1:]
        distances = lines[1].split()[1:]

        for i in range(len(speeds)):
            speeds[i] = int(speeds[i])
            distances[i] = int(distances[i])

        for i in range(len(speeds)):
            max_speed = speeds[i]
            values.append([])
            for s in range(speeds[i] + 1):
                values[i].append(s * (max_speed - s))
            
        betters = np.zeros(len(values))
        for i in range(len(values)):
            for j in range(len(values[i])):
                if values[i][j] > distances[i]:
                    betters[i] += 1
        
        print(np.prod(betters))