
#!/usr/bin/env python3
import sys

def main():
    with open(sys.argv[1]) as f:
        cargoPositions, instructions = f.read().split('\n\n')
    print("Part 1: {}".format(part1(cargoPositions, instructions)))
    print("Part 2: {}".format(part2(cargoPositions, instructions)))

def part1(cargoPositions, instructions):
    cargoYSize = int(cargoPositions.splitlines()[-1][-2])
    cargoXSize = len(cargoPositions.splitlines()[:-1])
    cargoStacks = [[None for x in range(cargoXSize)] for y in range(cargoYSize)]
    for idx, char in enumerate(cargoPositions):
        if ('A' <= char <= 'Z'):
            cargoStacks[(idx // 4) % cargoYSize][(idx // 4) // cargoYSize] = char
    cargoStacks = [list(filter(None, reversed(x))) for x in cargoStacks]
    for instruction in instructions.splitlines():
        _move, qty, _from, fromStack, _to, toStack = instruction.split()
        qty = int(qty)
        fromStack = int(fromStack) - 1
        toStack = int(toStack) - 1
        cargoStacks[toStack] += cargoStacks[fromStack][-qty:][::-1]
        cargoStacks[fromStack] = cargoStacks[fromStack][:-qty]
    return ''.join([cargoStacks[i][-1] for i in range(len(cargoStacks))])

def part2(cargoPositions, instructions):
    cargoStacks = [[line[i:i+4].strip() for i in range(0, len(line), 4)] for line in cargoPositions.split('\n')[:-1]]
    cargoStacks = [[cargoStacks[i][j] for i in range(len(cargoStacks))] for j in range(len(cargoStacks[0]))]
    cargoStacks = [list(filter(None, reversed(line))) for line in cargoStacks]
    for instruction in instructions.splitlines():
        _move, qty, _from, fromStack, _to, toStack = instruction.split()
        qty = int(qty)
        fromStack = int(fromStack) - 1
        toStack = int(toStack) - 1
        tempStack = []
        for _ in range(qty):
            tempStack.append(cargoStacks[fromStack].pop())
        cargoStacks[toStack] += tempStack[::-1]
    return ''.join([cargoStacks[i][-1][1] for i in range(len(cargoStacks))])

if __name__ == '__main__':
    main()

