import numpy as np

if __name__ == "__main__":
    values = []

    with open("input.txt", 'r') as f:
        lines = f.readlines()
        speeds = lines[0].split()[1:]
        distances = lines[1].split()[1:]

        speed = int(''.join(speeds))
        distance = int(''.join(distances))

        for s in range(speed + 1):
            values.append(s * (speed - s))
            
        betters = 0
        for i in range(len(values)):
            if values[i] > distance:
                betters += 1
        
        print(np.prod(betters))