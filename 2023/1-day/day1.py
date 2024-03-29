#!/usr/bin/env python3

# advent of code 2023 1. day solution
# https://adventofcode.com/2023/day/1
# Usage: python input1.txt

import sys

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print("Part 1: {}".format(part1(lines))) # 54081
    print("Part 2: {}".format(part2(lines))) # 54649

def part1(lines):
    sum = 0 
    for line in lines:
        for c in line:
            if c.isdigit():
                sum += 10 * int(c)
                break
        for c in line[::-1]:
            if c.isdigit():
                sum += int(c)
                break
    return sum

def check_for_first_word_number(line, current_idx, reverse=False):
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five" : 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    if len(line) < 3:
        return 0
    
    if reverse:
        if current_idx < 2:
            return 0
        if line[current_idx-2:current_idx + 1] in numbers:
            return numbers[line[current_idx-2:current_idx + 1 ]]
        if current_idx-3 >= 0 and line[current_idx-3:current_idx + 1] in numbers:
            return numbers[line[current_idx-3:current_idx + 1]]
        if current_idx-4 >= 0 and line[current_idx-4:current_idx + 1] in numbers:
            return numbers[line[current_idx-4:current_idx + 1]]
    
    if current_idx > len(line) - 3:
        return 0
    if line[current_idx:current_idx+3] in numbers:
        return numbers[line[current_idx:current_idx+3]]
    if current_idx + 4 <= len(line) and line[current_idx:current_idx+4] in numbers:
        return numbers[line[current_idx:current_idx+4]]
    if current_idx + 5 <= len(line) and line[current_idx:current_idx+5] in numbers:
        return numbers[line[current_idx:current_idx+5]]
    
    return 0

# Ugly code but it works
def part2(lines):
    sum = 0
    for line in lines:
        clean_line = line.strip()
        for i in range(len(clean_line)):
            if clean_line[i].isdigit():
                sum += 10 * int(clean_line[i])
                break
            else:
                number = check_for_first_word_number(clean_line, i)
                if number > 0:
                    sum += 10 * number
                    break
        for i in range(len(clean_line) - 1, -1, -1):
            if clean_line[i].isdigit():
                sum += int(clean_line[i])
                break
            else:
                number = check_for_first_word_number(clean_line, i, reverse=True)
                if number > 0:
                    sum += number
                    break
    return sum

if __name__ == '__main__':
    main()
