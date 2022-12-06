#!/usr/bin/env python3
import sys

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()[0]
        print(lines)
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))

def part1(lines):
    return [i for i in range(len(lines)) if len(set(lines[i - 4 : i])) == 4][0]


def part2(lines):
    return [i for i in range(len(lines)) if len(set(lines[i - 14 : i])) == 14][0]

if __name__ == '__main__':
    main()