# Advent of Code 2024
# Day 4: Ceres Search

from collections import defaultdict

# Read the input file
with open("2024/data/day04.txt", "r") as file:
    data = file.read().splitlines()

# Define the board
board = [list(line) for line in data]
NROWS, NCOLS = len(board), len(board[0])

# Search all the "X" and "M" in the board
X_positions, M_positions = [], []
for i in range(NROWS):
    for j in range(NCOLS):
        if board[i][j] == "X":
            X_positions.append((i, j))
        elif board[i][j] == "M":
            M_positions.append((i, j))

# Define the diagonal directions
diagonal_directions = [
    (1, -1),  # Down-Left
    (-1, -1),  # Up-Left
    (-1, 1),  # Up-Right
    (1, 1),  # Down-Right
]

# Define the directions
directions = [
    (1, 0),  # Down
    (0, -1),  # Left
    (-1, 0),  # Up
    (0, 1),  # Right
] + diagonal_directions


def is_inside(i, j):
    return 0 <= i < NROWS and 0 <= j < NCOLS


def search_xmas(i, j, direction, target):
    for char in target[1:]:
        i, j = i + direction[0], j + direction[1]
        if not is_inside(i, j) or board[i][j] != char:
            return False
    return True


count_1 = 0
for i, j in X_positions:
    for direction in directions:
        if search_xmas(i, j, direction, "XMAS"):
            count_1 += 1


# Print part 1 solution
print(f"Part 1: {count_1}")


A_positions = defaultdict(int)
for i, j in M_positions:
    for direction in diagonal_directions:
        if search_xmas(i, j, direction, "MAS"):
            di, dj = i + direction[0], j + direction[1]
            A_positions[(di, dj)] += 1


conut_2 = 0
for value in A_positions.values():
    if value == 2:
        conut_2 += 1


# Print part 2 solution
print(f"Part 2: {conut_2}")
