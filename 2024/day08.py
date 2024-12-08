# Advent of Code 2024
# Day 8: Resonant Collinearity

from collections import defaultdict
from itertools import combinations

# Read the input file
with open("2024/data/day08.txt", "r") as file:
    data = file.read().splitlines()

# Build a matrix from the input data
matrix = [list(line) for line in data]
NROWS, NCOLS = len(matrix), len(matrix[0])

# Find each char different to a "." and save its coordinates
coordinates = defaultdict(list)
for i, row in enumerate(matrix):
    for j, char in enumerate(row):
        if char != ".":
            coordinates[char].append((i, j))

# Find all pairs of coordinates for each key
pairs = dict()
for key, coords in coordinates.items():
    pairs[key] = list(combinations(coords, 2))

# Define the type of the pairs
type Pairs = dict[str, list[tuple[tuple[int, int], tuple[int, int]]]]


def is_in_matrix(i: int, j: int) -> bool:
    return 0 <= i < NROWS and 0 <= j < NCOLS


def get_uq_antinodes_1(pairs: Pairs) -> set[tuple[int, int]]:
    antinodes = set()
    for key, value in pairs.items():
        for (x1, y1), (x2, y2) in value:
            dx, dy = (x2 - x1), (y2 - y1)
            antinode1 = (x2 + dx, y2 + dy)
            antinode2 = (x1 - dx, y1 - dy)
            if is_in_matrix(*antinode1):
                antinodes.add(antinode1)
            if is_in_matrix(*antinode2):
                antinodes.add(antinode2)
    return antinodes


antinodes_1 = get_uq_antinodes_1(pairs)
print(f"Part 1: {len(antinodes_1)}")


def get_uq_antinodes_2(pairs: Pairs) -> set[tuple[int, int]]:
    antinodes = set()
    for key, value in pairs.items():
        for (x1, y1), (x2, y2) in value:
            dx, dy = (x2 - x1), (y2 - y1)
            while is_in_matrix(x2, y2):
                antinodes.add((x2, y2))
                x2, y2 = x2 + dx, y2 + dy
            while is_in_matrix(x1, y1):
                antinodes.add((x1, y1))
                x1, y1 = x1 - dx, y1 - dy
    return antinodes


antinodes_2 = get_uq_antinodes_2(pairs)
print(f"Part 2: {len(antinodes_2)}")
