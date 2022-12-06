#!/usr/bin/env python3
import sys


def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))

def part1(lines):
    totalSum = 0
    for line in lines:
        firstRange, secondRange = line.strip().split(",")
        firstStartRange, firstStopRange, secondStartRange, secondStopRange = map(int, firstRange.split("-") + secondRange.split("-"))
        if firstStartRange <= secondStartRange <= secondStopRange <= firstStopRange or secondStartRange <= firstStartRange <= firstStopRange <= secondStopRange:
            totalSum += 1
    return totalSum

def part2(lines):
    totalSum = 0
    for line in lines:
        firstRange, secondRange = line.strip().split(",")
        firstStartRange, firstStopRange, secondStartRange, secondStopRange = map(int, firstRange.split("-") + secondRange.split("-"))
        if firstStartRange <= secondStartRange <= firstStopRange or secondStartRange <= firstStartRange <= secondStopRange:
            totalSum += 1
    return totalSum

if __name__ == '__main__':
    main()