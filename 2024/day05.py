# Advent of Code 2024
# Day 5: Print Queue

from collections import defaultdict

# Read the input file
with open("2024/data/day05.txt", "r") as file:
    data = file.read().splitlines()

# Split the data into rules and print queue
rules = [line for line in data if "|" in line]
queue = [line for line in data if "," in line]

# Parse the rules
rules_dict = defaultdict(list)
for line in rules:
    key, value = map(int, line.split("|"))
    rules_dict[key].append(value)

# Parse the print queue
queue_list = []
for line in queue:
    queue_list.append(list(map(int, line.split(","))))


def is_ordered(queue: list[int]) -> bool:
    for i, item in enumerate(queue):
        values = rules_dict.get(item, [])
        others = queue[i + 1 :]
        if not all(other in values for other in others):
            return False
    return True


# Get the queues that are ordered given the rules
ordered_queues = [queue for queue in queue_list if is_ordered(queue)]


def middle_item(queue: list[int]) -> int:
    return queue[len(queue) // 2]


middle_items_1 = [middle_item(queue) for queue in ordered_queues]
print(f"Part 1: {sum(middle_items_1)}")


# Get the queues that are not ordered given the rules
unordered_queues = [queue for queue in queue_list if not is_ordered(queue)]


def order_items(queue: list[int]) -> list[int]:
    for j in range(len(queue)):
        i = len(queue) - j - 1
        if not is_ordered(queue[i:]):
            queue[i + 1], queue[i] = queue[i], queue[i + 1]
            queue[i:] = order_items(queue[i:])
    return queue


middle_items_2 = [middle_item(order_items(queue)) for queue in unordered_queues]
print(f"Part 2: {sum(middle_items_2)}")
