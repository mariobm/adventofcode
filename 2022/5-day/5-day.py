
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
    cargoStacks = [[char if ('A' <= char <= 'Z') else None for idx, char in enumerate(cargoPositions) if idx % 4 == 0 and ('A' <= char <= 'Z')] for y in range(cargoYSize)]
    cargoStacks = [list(filter(None, reversed(x))) for x in cargoStacks]
    for instruction in instructions.splitlines():
        _move, qty, _from, fromStack, _to, toStack = instruction.split()
        qty = int(qty)
        fromStack = int(fromStack) - 1
        toStack = int(toStack) - 1
        for _ in range(qty):
            cargoStacks[toStack].append(cargoStacks[fromStack].pop())
    return ''.join([cargoStacks[i][-1] for i in range(len(cargoStacks))])

def part2(cargoPositions, instructions):
    cargoStacks = [[line[i:i+4].strip() if i % 4 == 0 and ('A' <= line[i:i+4].strip() <= 'Z') else None for i in range(0, len(line), 4)] for line in cargoPositions.split('\n')[:-1]]
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
        for _ in range(qty):
            cargoStacks[toStack].append(tempStack.pop())
    return ''.join([cargoStacks[i][-1][1] for i in range(len(cargoStacks))])

if __name__ == '__main__':
    main()
