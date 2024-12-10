# Advent of Code 2024
# Day 10: Hoof It

# Read the input file
with open("2024/data/day10.txt", "r") as file:
    data = file.read().splitlines()


# Build a board from the input data
board = [list(map(int, line)) for line in data]
NROWS, NCOLS = len(board), len(board[0])


def get_start_positions() -> list[tuple[int, int]]:
    return [(i, j) for i in range(NROWS) for j in range(NCOLS) if board[i][j] == 0]


def get_directions() -> list[tuple[int, int]]:
    return [(0, 1), (1, 0), (0, -1), (-1, 0)]


def count_paths(
    board: list[list[int]],
    start: tuple[int, int],
    last: int = -1,
) -> tuple[set[tuple[int, int]], int]:
    x, y = start
    if x < 0 or x >= NROWS or y < 0 or y >= NCOLS:
        return set(), 0
    if board[x][y] - last != 1:
        return set(), 0
    if board[x][y] == 9:
        return set([(x, y)]), 1
    total_nine_positions = set()
    total_paths = 0
    for direction in get_directions():
        x_new, y_new = x + direction[0], y + direction[1]
        nine_positions, n_paths = count_paths(board, (x_new, y_new), board[x][y])
        total_nine_positions.update(nine_positions)
        total_paths += n_paths
    return total_nine_positions, total_paths


# Find all possibles paths from a 0 to a 9
n_paths, n_distinct_paths = 0, 0
for start in get_start_positions():
    nine_positions, distinct_paths = count_paths(board, start)
    n_paths += len(nine_positions)
    n_distinct_paths += distinct_paths


print(f"Part 1: {n_paths}")
print(f"Part 2: {n_distinct_paths}")
