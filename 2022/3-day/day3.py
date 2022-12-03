#!/usr/bin/env python3
import sys


def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))

def part1(lines):
    indexPriority = dict(zip(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), range(1, 53)))      
    return sum([indexPriority[(set(line[:len(line)//2]) & set(line[len(line)//2:])).pop()] for line in lines])

def part2(lines):
    indexPriority = dict(zip(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), range(1, 53)))  
    return sum([indexPriority[(set(i.strip()) & set(j.strip()) & set(k.strip())).pop()] for i,j,k in zip(*[iter(lines)]*3)])

if __name__ == '__main__':
    main()