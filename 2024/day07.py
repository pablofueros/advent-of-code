# Advent of Code 2024
# Day 7: Bridge Repair

from itertools import product

# Read the input file
with open("2024/data/day07.txt", "r") as file:
    data = file.read().splitlines()

# Split the data into two parts
test_values, ecuations = [], []
for line in data:
    test_value, ecuation = line.split(": ")
    test_values.append(int(test_value))
    ecuations.append(list(map(int, ecuation.split(" "))))


def is_valid(test_value, ecuation, operators) -> bool:
    # Eval the ecuation from left to right
    result = ecuation[0]
    for value, operator in zip(ecuation[1:], operators):
        if operator == "+":
            result += value
        elif operator == "*":
            result *= value
        elif operator == "||":
            result = int(str(result) + str(value))
    return result == test_value


def compute_valid_ecuations(test_values, ecuations, operators):
    valid_values, invalid_inds = [], []
    for ind, (test_value, ecuation) in enumerate(zip(test_values, ecuations)):
        n_operators = len(ecuation) - 1
        for comb in product(operators, repeat=n_operators):
            if is_valid(test_value, ecuation, comb):
                valid_values.append(test_value)
                break
        else:
            invalid_inds.append(ind)
    return valid_values, invalid_inds


valid_values_1, inds = compute_valid_ecuations(test_values, ecuations, ["+", "*"])
print(f"Part 1: {sum(valid_values_1)}")

# Remove the invalid values and ecuations
inv_values = [test_values[ind] for ind in inds]
inv_equations = [ecuations[ind] for ind in inds]

valid_values_2, _ = compute_valid_ecuations(inv_values, inv_equations, ["*", "+", "||"])
print(f"Part 2: {sum(valid_values_1) + sum(valid_values_2)}")
