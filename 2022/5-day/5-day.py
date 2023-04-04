
#!/usr/bin/env python3
import sys

def main():
    with open(sys.argv[1]) as f:
        cP, i = f.read().split('\n\n')
    print("Part 1: {}".format(p1(cP, i)))
    print("Part 2: {}".format(p2(cP, i)))

def p1(cp, i):
    cy = int(cp.splitlines()[-1][-2])
    cx = len(cp.splitlines()[:-1])
    cs = [[None for x in range(cx)] for y in range(cy)]
    for idx, char in enumerate(cp):
        if ('A' <= char <= 'Z'):
            cs[(idx // 4) % cy][(idx // 4) // cy] = char
    cs = [list(filter(None, reversed(x))) for x in cs]
    for instruction in i.splitlines():
        _, q, _, fs, _, ts = instruction.split()
        q = int(q)
        fs = int(fs) - 1
        ts = int(ts) - 1
        for _ in range(q):
            cs[ts].append(cs[fs].pop())
    return ''.join([cs[i][-1] for i in range(len(cs))])

def p2(cp, i):
    cs = [[line[i:i+4].strip() for i in range(0, len(line), 4)] for line in cp.split('\n')[:-1]]
    cs = [[cs[i][j] for i in range(len(cs))] for j in range(len(cs[0]))]
    cs = [list(filter(None, reversed(line))) for line in cs]
    for instruction in i.splitlines():
        _, q, _, fs, _, ts = instruction.split()
        q = int(q)
        fs = int(fs) - 1
        ts = int(ts) - 1
        ts = []
        for _ in range(q):
            ts.append(cs[fs].pop())
        for _ in range(q):
            cs[ts].append(ts.pop())
    return ''.join([cs[i][-1][1] for i in range(len(cs))])

if __name__ == '__main__':
    main()

