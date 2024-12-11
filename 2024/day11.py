# Advent of Code 2024
# Day 11: Plutonian Pebbles

from functools import cache

# Read the input file
with open("2024/data/day11.txt", "r") as file:
    data = list(map(int, file.read().split()))


@cache
def process(stone: int, step: int) -> int:
    if step == 0:
        return 1
    elif stone == 0:
        return process(1, step - 1)
    elif len(str(stone)) % 2 == 0:
        sstone = str(stone)
        n = len(sstone) // 2
        lpart, rpart = int(sstone[:n]), int(sstone[n:])
        return process(lpart, step - 1) + process(rpart, step - 1)
    else:
        return process(2024 * stone, step - 1)


def transformed_stones_sum(stone_list: list, steps: int) -> int:
    return sum(process(stone, steps) for stone in stone_list)


print(f"Part 1: {transformed_stones_sum(data, 25)}")
print(f"Part 2: {transformed_stones_sum(data, 75)}")
