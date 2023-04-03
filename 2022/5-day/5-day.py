#!/usr/bin/env python3
import sys

def main():
    with open(sys.argv[1]) as f:
        cargo, instructions = f.read().split('\n\n')
    print("Part 1: {}".format(part1(cargo, instructions)))
    print("Part 2: {}".format(part2(cargo, instructions)))

def part1(cargo, instructions):
    y = int(cargo.splitlines()[-1][-2])
    x = len(cargo.splitlines()[:-1])
    s = [[None for x in range(x)] for y in range(y)]
    for idx, char in enumerate(cargo):
        if ('A' <= char <= 'Z'):
            s[(idx // 4) % y][(idx // 4) // y] = char
    s = [list(filter(None, reversed(x))) for x in s]
    for i in instructions.splitlines():
        m, q, f, fs, t, ts = i.split()
        q, fs, ts = int(q), int(fs) - 1, int(ts) - 1
        for _ in range(q):
            s[ts].append(s[fs].pop())
    return ''.join([s[i][-1] for i in range(len(s))])

def part2(cargo, instructions):
    s = [[line[i:i+4].strip() for i in range(0, len(line), 4)] for line in cargo.split('\n')[:-1]]
    s = [[s[i][j] for i in range(len(s))] for j in range(len(s[0]))]
    s = [list(filter(None, reversed(line))) for line in s]
    for i in instructions.splitlines():
        m, q, f, fs, t, ts = i.split()
        q, fs, ts, temp = int(q), int(fs) - 1, int(ts) - 1, []
        for _ in range(q):
            temp.append(s[fs].pop())
        for _ in range(q):
            s[ts].append(temp.pop())
    return ''.join([s[i][-1][1] for i in range(len(s))])

if __name__ == '__main__':
    main()
    
