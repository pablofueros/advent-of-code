# Advent of Code 2024
# Day 14: Restroom Redoubt

import re
from collections import defaultdict

# Read the input file
with open("2024/data/day14.txt", "r") as file:
    data = file.read().splitlines()


# Parse the input data
positions, velocities = [], []
for line in data:
    x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
    positions.append((x, y))
    velocities.append((vx, vy))


# Define the board details
NCOLS, NROWS = 101, 103
ITERS = 100


def compute_next(position, velocity):
    (x, y), (vx, vy) = position, velocity
    return (x + vx) % NCOLS, (y + vy) % NROWS


def count_values(positions):
    values = defaultdict(lambda: 0)
    for position in positions:
        values[position] += 1
    return values


def compute_final_positions(positions, velocities, iters):
    for _ in range(iters):
        next_positions = []
        for position, velocity in zip(positions, velocities):
            x_new, y_new = compute_next(position, velocity)
            next_positions.append((x_new, y_new))
        positions = next_positions
    return count_values(positions)


# Calculate the final positions after ITERS iterations
final_positions = compute_final_positions(positions, velocities, ITERS)


quadrants = [0, 0, 0, 0]
for final_pos, value in final_positions.items():
    x, y = final_pos
    if x < NCOLS // 2 and y < NROWS // 2:
        quadrants[0] += value
    elif x > NCOLS // 2 and y < NROWS // 2:
        quadrants[1] += value
    elif x < NCOLS // 2 and y > NROWS // 2:
        quadrants[2] += value
    elif x > NCOLS // 2 and y > NROWS // 2:
        quadrants[3] += value
    else:
        continue


prod = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
print(f"Part 1: {prod}")


def simulate_until_tree(positions, velocities):
    ITER = 0
    positions_count = count_values(positions)
    while max(positions_count.values()) != 1:
        next_positions = []
        for position, velocity in zip(positions, velocities):
            next_positions.append(compute_next(position, velocity))
        positions = next_positions
        positions_count = count_values(positions)
        ITER += 1
    return ITER


iter = simulate_until_tree(positions, velocities)
print(f"Part 2: {iter}")
