import math

def sled(trees, right, down):
    height = len(trees)
    width = len(trees[0])
    count = x = y = 0
    while y < height - down:
        x = (x + right) % width
        y += down
        if trees[y][x]:
            count += 1
    return count

with open('input.txt') as f:
    data = [[c == '#' for c in l] for l in f.read().splitlines()]

print(sled(data, 3, 1))