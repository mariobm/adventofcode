#!/usr/bin/env python3
import sys
import math

def main():
    lines = open(sys.argv[1]).readlines()
    grid = []
    for line in lines:
        grid.append([int(char) for char in line.strip()])
    print("Part 1: {}".format(part1(grid)))
    print("Part 2: {}".format(part2(grid)))

def lookup(grid, currentElement, coordinates, step):
    x, y = coordinates
    newX = x + step[0]
    newY = y + step[1]
    if 0 <= newY < len(grid) and 0 <= newX < len(grid[y]):
        newElement = grid[newY][newX]
        if newElement < currentElement:
            return lookup(grid, currentElement, (newX, newY), step)
        return 0
    return 1

def lookup2(grid, currentElement, coordinates, step, count = 0):
    x, y = coordinates
    newX = x + step[0]
    newY = y + step[1]
    if 0 <= newY < len(grid) and 0 <= newX < len(grid[y]):
        newElement = grid[newY][newX]
        count += 1
        if newElement < currentElement:
            return lookup2(grid, currentElement, (newX, newY), step, count)
        return count
    return count

def part1(grid):
    maxes = len(grid) * 2 + len(grid[0]) * 2 - 4
    smeriNeba = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            maxes += 1 in [lookup(grid, grid[y][x], (x, y), smer) for smer in smeriNeba]
    return maxes

def part2(grid):
    smeriNeba = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    productsList = []
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            productsList.append(math.prod([lookup2(grid, grid[y][x], (x, y), smer) for smer in smeriNeba]))
    return max(productsList)

if __name__ == '__main__':
    main()