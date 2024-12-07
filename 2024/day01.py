# Advent of Code 2024
# Day 1: Historian Hysteria

# Read the input file
with open("2024/data/day01.txt", "r") as file:
    data = file.read().splitlines()

# Split the data into two lists of integers
left, right = [], []
for line in data:
    nl, nr = line.split()
    left.append(int(nl))
    right.append(int(nr))

# Sort both lists
left.sort()
right.sort()

# Compute the differences
diffs = [abs(x - y) for x, y in zip(left, right)]

# Print the part 1 solution
print(f"Part 1: {sum(diffs)}")

# Compute the number of times a number in
# the left list appears in the right list
map = {}
ind = 0
for nl in left:
    count = 0
    for nr in right[ind:]:
        if nl == nr:
            count += 1
        elif nr > nl:
            break
    map[nl] = count
    ind += count

# Compute the similarity score
score = [k * v for k, v in map.items()]
print(f"Part 2: {sum(score)}")
