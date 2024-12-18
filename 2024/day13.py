# Advent of Code 2024
# Day 11: Plutonian Pebbles


import re
from math import gcd

# Read the input file
with open("2024/data/day13.txt", "r") as file:
    data = file.read().splitlines()


# Regular expressions for each line type
button_a_pattern = r"^Button A: X([+-]?\d+), Y([+-]?\d+)"
button_b_pattern = r"^Button B: X([+-]?\d+), Y([+-]?\d+)"
prize_pattern = r"^Prize: X=([+-]?\d+), Y=([+-]?\d+)"


equations = []
for i in range(0, len(data), 4):
    chunck = data[i : i + 4]
    for line in chunck:
        if match := re.match(button_a_pattern, line):
            x1, y1 = int(match.group(1)), int(match.group(2))
        elif match := re.match(button_b_pattern, line):
            x2, y2 = int(match.group(1)), int(match.group(2))
        elif match := re.match(prize_pattern, line):
            x, y = int(match.group(1)), int(match.group(2))
        else:
            continue
    equations.append([[x1, x2, x], [y1, y2, y]])


def has_int_solution(equation: list) -> bool:
    alpha = gcd(equation[0][0], equation[0][1])
    beta = gcd(equation[1][0], equation[1][1])
    return (equation[0][2] % alpha == 0) and (equation[1][2] % beta == 0)


def solve(equation: list) -> tuple:
    a1, b1, c1 = equation[0]
    a2, b2, c2 = equation[1]
    det = a1 * b2 - a2 * b1
    if det == 0:
        return (0, 0)
    det_x = c1 * b2 - c2 * b1
    det_y = a1 * c2 - a2 * c1
    if det_x % det != 0 or det_y % det != 0:
        return 0, 0
    return det_x // det, det_y // det


A_WEIGHT, B_WEIGHT = 3, 1

min_tokens_1 = 0
for equation in equations:
    if not has_int_solution(equation):
        continue
    a, b = solve(equation)
    if a < 0 or b < 0:
        continue
    if a > 100 or b > 100:
        continue
    min_tokens_1 += a * A_WEIGHT + b * B_WEIGHT


print(f"Part 1: {min_tokens_1}")

DELTA = 10000000000000

min_tokens_2 = 0
for equation in equations:
    equation[0][2] += DELTA
    equation[1][2] += DELTA
    if not has_int_solution(equation):
        continue
    a, b = solve(equation)
    if a < 0 or b < 0:
        continue
    min_tokens_2 += a * A_WEIGHT + b * B_WEIGHT


print(f"Part 2: {min_tokens_2}")
