#!/usr/bin/env python3
import sys

class Node:
    def __init__(self, data, size, parent=None):
        self.data = data
        self.parent = parent
        self.children = []
        self.size = size

    def add_child(self, child):
        self.children.append(child)
        if child.size > 0:
            self.propagate_size(child.size)

    def propagate_size(self, fileSize):
        self.size += fileSize
        if self.parent:
            self.parent.propagate_size(fileSize)
    
    def traverse(self):
        for child in self.children:
            yield child
            yield from child.traverse()

def buildTree(lines):
    root = Node("/", 0)
    currentParent = root
    for line in lines:
        command = line.strip().split()
        if command[1] == "cd":
            x, y, z = command
        else:
            x, y = command

        if y == "cd":
            if z == "..":
                currentParent = currentParent.parent
            elif z == "/":
                currentParent = root
            else:
                for child in currentParent.children:
                    if child.data == z:
                        currentParent = child
                        break
                else:
                    child = Node(z, 0, currentParent)
                    currentParent.add_child(child)
                    currentParent = child
            continue
        elif y == "ls" or x == "dir":
            continue
        size = int(x)
        currentParent.propagate_size(size)
    return root

def main():
    lines = open(sys.argv[1]).readlines()
    print("Part 1: {}".format(part1(buildTree(lines))))
    print("Part 2: {}".format(part2(buildTree(lines))))

def part1(tree1):
    return sum(child.size for child in tree1.traverse() if child.size <= 100000)

def part2(tree2):
    currentFreeSpace = 70000000 - tree2.size
    sortedNodes = sorted(tree2.traverse(), key=lambda x: x.size)
    for node in sortedNodes:
        if currentFreeSpace + node.size >= 30000000:
            return node.size
    return tree2.size

if __name__ == '__main__':
    main()