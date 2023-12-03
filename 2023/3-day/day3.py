#!/usr/bin/env python3

# advent of code 2023 3. day solution
# https://adventofcode.com/2023/day/3
# Usage: python input1.txt

import sys, re
from collections import defaultdict

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print("Part 1: {}".format(part1(lines))) # 525181
    print("Part 2: {}".format(part2(lines))) # 

def get_all_numbers_with_cooridnates(lines):
    all_numbers = defaultdict(int)
    for y, line in enumerate(lines):
        for number in re.finditer(r'\d+', line):
            digits = len(number.group())
            all_numbers[(number.start(), y)] = int(number.group())
            for i in range(1, digits):
                if all_numbers[(number.start() + i, y)]:
                    print("Overlapping numbers")
                all_numbers[(number.start() + i, y)] = int(number.group())
    return all_numbers

def part1(lines):
    cumulative_sum = 0
    all_numbers = get_all_numbers_with_cooridnates(lines)
    neighbor_offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for y, current_line in enumerate(lines):
        for x, ch in enumerate(current_line.strip()):
            if not ch.isdigit() and ch != ".":
                last_added = None
                for dx, dy in neighbor_offsets:
                    nx, ny = x + dx, y + dy
                    if all_numbers.get((nx, ny)) and all_numbers[(nx, ny)] != last_added:
                        cumulative_sum += all_numbers[(nx, ny)]
                        last_added = all_numbers[(nx, ny)]
    return cumulative_sum

def part2(lines):
    cumulative_sum = 0
    all_numbers = get_all_numbers_with_cooridnates(lines)
    neighbor_offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for y, current_line in enumerate(lines):
        for x, ch in enumerate(current_line.strip()):
            if ch == "*":
                last_added = None
                adjacent_numbers = []
                for dx, dy in neighbor_offsets:
                    nx, ny = x + dx, y + dy
                    if all_numbers.get((nx, ny)) and all_numbers[(nx, ny)] != last_added:
                        last_added = all_numbers[(nx, ny)]
                        adjacent_numbers.append(all_numbers[(nx, ny)])
                if len(adjacent_numbers) == 2:
                    cumulative_sum += adjacent_numbers[0] * adjacent_numbers[1]
    return cumulative_sum

if __name__ == '__main__':
    main()
