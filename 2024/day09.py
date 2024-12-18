# Advent of Code 2024
# Day 9: Disk Fragmenter

from collections import deque

# Read the input file
with open("2024/data/day09.txt", "r") as file:
    data = file.read()


# Compute the disk map block-representation
final, file_id = [], 0
items, spaces = deque(), deque()
items_len, spaces_len = [], []
current_pos = 0
for ind, char in enumerate(data):
    pos_range = range(current_pos, current_pos + int(char))
    block = [ind + i for i in pos_range]
    if ind % 2 == 0:
        final.extend([str(file_id)] * int(char))
        items.extend(block)
        if len(block) > 0:
            items_len.append((block[0], len(block), str(file_id)))
        file_id += 1
    else:
        final.extend(["."] * int(char))
        spaces.extend(block)
        if len(block) > 0:
            spaces_len.append((block[0], len(block), "."))
    current_pos += int(char) - 1


def can_continue_1(first_space: int, last_item: int) -> bool:
    return first_space < last_item


def compress_repr_1(final: list, spaces: deque, items: deque) -> list:
    while can_continue_1(spaces[0], items[-1]):
        final[spaces[0]] = final[items[-1]]
        final[items[-1]] = "."
        spaces.popleft()
        items.pop()
    return final


c_repr_1 = compress_repr_1(final[:], spaces, items)
checksum_1 = [i * int(x) for (i, x) in enumerate(c_repr_1) if x != "."]
print(f"Part 1: {sum(checksum_1)}")


def can_continue_2(items_len: list) -> bool:
    return len(items_len) > 0


def compress_repr_2(final: list, spaces_len, items_len) -> list:
    while can_continue_2(items_len):
        for ind, space_len in enumerate(spaces_len):
            item_len = items_len[-1]
            if space_len[1] < item_len[1]:
                continue
            if space_len[0] > item_len[0]:
                continue
            # Update the final list
            space_slice = slice(space_len[0], space_len[0] + item_len[1])
            item_slice = slice(item_len[0], item_len[0] + item_len[1])
            final[space_slice] = final[item_slice]
            final[item_slice] = ["."] * item_len[1]
            # Update the space_len
            new_index = space_len[0] + item_len[1]
            new_len = space_len[1] - item_len[1]
            spaces_len[ind] = (new_index, new_len, ".")
            break
        items_len.pop()
    return final


c_repr_2 = compress_repr_2(final[:], spaces_len, items_len)
checksum_2 = [i * int(x) for (i, x) in enumerate(c_repr_2) if x != "."]
print(f"Part 2: {sum(checksum_2)}")
