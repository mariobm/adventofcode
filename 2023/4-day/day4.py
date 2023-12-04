#!/usr/bin/env python3

# advent of code 2023 3. day solution
# https://adventofcode.com/2023/day/3
# Usage: python input1.txt

import sys
from collections import defaultdict

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print("Part 1: {}".format(part1(lines))) # 21088
    print("Part 2: {}".format(part2(lines))) # 6874754

def part1(cards):
    total_points = 0
    for card in cards:
       winning, scratched = card.split(":")[1].split("|")
       winning_set = set(map(int, winning.split()))
       scratched_set = set(map(int, scratched.split()))
       intersection = winning_set & scratched_set
       total_points += 1 << len(intersection)-1 if len(intersection) else 0
    return total_points

def part2(cards):
    card_wins = defaultdict(int)
    for game_number, card in enumerate(cards, 1):
       card_wins[game_number] += 1
       winning, scratched = card.split(":")[1].split("|")
       winning_set = set(map(int, winning.split()))
       scratched_set = set(map(int, scratched.split()))
       intersection = winning_set & scratched_set
       for number in range(game_number + 1, game_number + 1 + len(intersection)):
          card_wins[number] += card_wins[game_number]
    return sum(card_wins.values())

if __name__ == '__main__':
    main()
