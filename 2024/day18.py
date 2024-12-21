# Advent of Code 2024
# Day 18: RAM Run


# Read the input file
with open("2024/data/day18.txt", "r") as file:
    data = file.read().splitlines()

# Parse the input data
corrupted = []
for line in data:
    x, y = map(int, line.split(","))
    corrupted.append((x, y))

# Define the board details
NROWS, NCOLS = 70, 70
START, END = (0, 0), (NROWS, NCOLS)
INIT_OBS = 1024

# Define the directions
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_inside(x, y):
    return 0 <= x < NROWS + 1 and 0 <= y < NCOLS + 1


def steps_in_shortest_path(start, end, obstacles):
    """Implement a breadth-first search to find the shortest path."""
    queue = [(start, 0)]
    visited = {start}
    while queue:
        (x, y), steps = queue.pop(0)
        if (x, y) == end:
            return steps
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (
                is_inside(new_x, new_y)
                and (new_x, new_y) not in visited
                and (new_x, new_y) not in obstacles
            ):
                queue.append(((new_x, new_y), steps + 1))
                visited.add((new_x, new_y))
    return -1


print(f"Part 1: {steps_in_shortest_path(START, END, corrupted[:INIT_OBS])}")


def first_blocking_obstacle(start, end, obstacles):
    for i in range(INIT_OBS, len(obstacles)):
        # print(f"Checking obstacle {i + 1} of {len(obstacles)}")
        if steps_in_shortest_path(start, end, obstacles[: i + 1]) == -1:
            return obstacles[i]


print(f"Part 2: {first_blocking_obstacle(START, END, corrupted)}")
