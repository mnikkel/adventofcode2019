#!/usr/bin/env python
# -*- coding: utf-8 -*-
GRID_SIZE = 20000
START = 10000

WIRES = []
CROSSED = []
DISTANCE = []
STEPS = []
with open('input') as f:
    for line in f:
        WIRES.append(line.rstrip())

W1 = WIRES[0].split(',')
W2 = WIRES[1].split(',')

GRID = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def place_wire(wire, name):
    pos = [START, START]
    key = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
    step = 0
    for link in wire:
        direction = link[:1]
        distance = int(link[1:])
        for _ in range(distance):
            step += 1
            pos = [x + y for x, y in zip(key[direction], pos)]
            if GRID[pos[0]][pos[1]] is None:
                GRID[pos[0]][pos[1]] = [name, step]
            elif GRID[pos[0]][pos[1]][0] != name:
                CROSSED.append([pos[0]-START, pos[1]-START, GRID[pos[0]][pos[1]][1], step])
                GRID[pos[0]][pos[1]] = 'cross'


place_wire(W1, 'w1')
place_wire(W2, 'w2')

for coord in CROSSED:
    DISTANCE.append(abs(coord[0]) + abs(coord[1]))
    STEPS.append(coord[2] + coord[3])

print(min(DISTANCE))
print(min(STEPS))
