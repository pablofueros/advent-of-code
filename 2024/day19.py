# Advent of Code 2024
# Day 19: Linen Layout

from collections import defaultdict
from functools import cache

# Read the input file
with open("2024/data/day19.txt", "r") as file:
    data = file.read().splitlines()


# Parse the input data
subpatterns = list(map(str, data[0].split(", ")))
patterns = data[2:]

# Create a dictionary with the first character of each subpattern
first_char = defaultdict(list)
for subpattern in subpatterns:
    first_char[subpattern[0]].append(subpattern)


@cache
def is_pattern_matching(pattern: str, chars_left=None) -> bool:
    if chars_left is None:
        chars_left = len(pattern)
    for subpattern in first_char[pattern[0]]:
        if not pattern.startswith(subpattern):
            continue
        if chars_left == len(subpattern):
            return True
        if is_pattern_matching(
            pattern[len(subpattern) :],
            chars_left - len(subpattern),
        ):
            return True
    return False


matching_results = [is_pattern_matching(pattern) for pattern in patterns]
print(f"Part 1: {sum(matching_results)}")


@cache
def count_matching_patterns(pattern: str, chars_left=None) -> int:
    if chars_left is None:
        chars_left = len(pattern)
    count = 0
    for subpattern in first_char[pattern[0]]:
        if not pattern.startswith(subpattern):
            continue
        if chars_left == len(subpattern):
            count += 1
        else:
            count += count_matching_patterns(
                pattern[len(subpattern) :],
                chars_left - len(subpattern),
            )
    return count


pattern_match_counts = [count_matching_patterns(pattern) for pattern in patterns]
print(f"Part 2: {sum(pattern_match_counts)}")
