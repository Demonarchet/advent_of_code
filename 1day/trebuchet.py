import numpy as np

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                "six": 6, "seven": 7, "eight": 8, "nine": 9}

text = open("input.txt", "r")
lines = text.readlines()

total_cost = 0
for line in lines:
    line = line.split()
    for t, word in enumerate(line):
        values = []
        indexes =  []

        # Check if there is there are lettered numbers in the word
        for number in numbers:
            nb_occ = word.count(number)

            # If there is only 1 occurence of the number in the word add it to the list
            if nb_occ == 1:
                values.append(numbers_dict[number])
                indexes.append(word.index(number))

            # If there are more than 1 occurence of the number in the word, then add all of them
            elif nb_occ > 1:
                word_copy = word
                total_idx = 0
                for i in range(nb_occ):
                    idx = word_copy.find(number)
                    total_idx += idx + 1
                    values.append(numbers_dict[number])
                    indexes.append(total_idx)
                    word_copy = word_copy[idx+1:]

        # Check if there are numbers in the word
        for j, charac in enumerate(word):
            if charac.isdigit():
                values.append(int(charac))
                indexes.append(j)
        
        values = np.array(values)
        indexes = np.array(indexes)

        line_result = 0
        if len(values) == 1:
            line_result = 10 * values[0] + values[0]
        elif len(values) > 1:
            maxi = np.argmax(indexes)
            mini = np.argmin(indexes)
            line_result = 10 * values[mini] + values[maxi]

        total_cost += line_result
print(total_cost)