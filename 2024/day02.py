# Advent of Code 2024
# Day 2: Red-Nosed Reports


# Read the input file
with open("2024/data/day02.txt", "r") as file:
    data = file.read()

# Split each line into a list of integers
reports = []
for line in data.splitlines():
    reports.append([int(x) for x in line.split()])


def is_decreasing(report: list[int]) -> bool:
    sorted_report = sorted(report)
    return report == sorted_report[::-1]


def is_increasing(report: list[int]) -> bool:
    sorted_report = sorted(report)
    return report == sorted_report


def check_adjacent(report: list[int]) -> bool:
    diffs = [abs(x - y) for x, y in zip(report[:-1], report[1:])]
    return min(diffs) >= 1 and max(diffs) <= 3


def is_safe(report: list[int]) -> bool:
    if not check_adjacent(report):
        return False
    if is_increasing(report):
        return True
    if is_decreasing(report):
        return True
    return False


# Check how many reports are safe
result = sum([is_safe(report) for report in reports])
print(f"Part 1: {result}")


def is_tolerably_safe(report: list[int]) -> bool:
    if is_safe(report):
        return True
    # Make len(report) copies, each one without one element
    reports = [report[:i] + report[i + 1 :] for i in range(len(report))]
    for r in reports:
        if is_safe(r):
            return True
    return False


# Check how many reports are tolerably safe
result = sum([is_tolerably_safe(report) for report in reports])
print(f"Part 2: {result}")
