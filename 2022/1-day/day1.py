import numpy as np
with open('input1.txt') as f:
    firstLine = f.readline()
    maxCal = int(firstLine)
    currentSumArray = []
    currentSum = maxCal
    for line in f:
        if line != '\n':
            currentSum += int(line)
        else: 
            currentSumArray.append(currentSum)
            currentSum = 0
    currentSumArray.append(currentSum)
    # max elf
    top3 = np.sort(currentSumArray)[-3:]
    print(len(currentSumArray))
    print('Top 3 elves: ', top3)
    print('Total sum of top 3 elves: ', np.sum(top3))
