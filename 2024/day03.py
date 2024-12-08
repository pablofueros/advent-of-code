# Advent of Code 2024
# Day 3: Mull It Over

import re

# Read the input file into one string
with open("2024/data/day03.txt", "r") as file:
    data = file.read()

# Define the mul pattern and find all matches
pattern_mul = re.compile(r"mul\(\b\d{1,3}\b,\b\d{1,3}\b\)")
matches_mul = list(pattern_mul.finditer(data))

# Extract the numbers from the matches and multiply them
nums_1 = [re.findall(r"\d{1,3}", match.group()) for match in matches_mul]

result_1 = [int(x) * int(y) for x, y in nums_1]
print(f"Part 1: {sum(result_1)}")

# Define the do pattern and find the indices of the matches
pattern_do = re.compile(r"\bdo\(\)")
matches_do = list(pattern_do.finditer(data))

# Define the don't pattern and find the indices of the matches
pattern_dont = re.compile(r"\bdon't\(\)")
matches_dont = list(pattern_dont.finditer(data))

# Create a dictionary and a list of the starts of the matches
starts_dict, starts_list = dict(), []
for match in matches_mul:
    starts_dict[match.start()] = match.group()
    starts_list.append(match.start())
for match in matches_do:
    starts_dict[match.start()] = match.group()
    starts_list.append(match.start())
for match in matches_dont:
    starts_dict[match.start()] = match.group()
    starts_list.append(match.start())

# Sort the list of starts
sorted_starts = sorted(starts_list)

# Extract the numbers from the matches and multiply them
nums, enabled = [], True
for start in sorted_starts:
    match = starts_dict[start]
    if enabled and "mul" in match:
        nums.append(re.findall(r"\d{1,3}", match))
    elif "do()" == match:
        enabled = True
    elif "don't()" == match:
        enabled = False

result_2 = [int(x) * int(y) for x, y in nums]
print(f"Part 2: {sum(result_2)}")
