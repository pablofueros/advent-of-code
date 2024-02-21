# Advent of Code 2023
# Day 8: Wasteland

from dataclasses import dataclass
from math import lcm


def element_attrs(info: str) -> tuple[str, str, str]:
    name, tuple = info.split("=")
    left, right = tuple.split(",")
    return name[:3], left[2:], right[1:4]


@dataclass
class Node:
    name: str
    left: str
    right: str

    def __getitem__(self, key: str) -> str:
        return getattr(self, key)


@dataclass
class NavigationMap:
    elements: dict[str, Node]
    steps: list[str]

    @property
    def n_steps(self) -> int:
        return len(self.steps)

    def cycle_len(self, name: str, part1: bool) -> int:
        iter, num = 0, self.n_steps
        while name != "ZZZ" if part1 else name[-1] != "Z":
            node = self.elements[name]
            move = self.steps[iter % num]
            name = node[move]
            iter += 1
        return iter


if __name__ == "__main__":

    def result(map: NavigationMap, names: list[str], part1: bool) -> int:
        lengths = [map.cycle_len(name, part1) for name in names]
        return lcm(*lengths)

    with open("data/8_wasteland.txt", "r") as file:
        data = file.read().splitlines()

    # Split the data into elements (as dict) and instructions
    element_list = [Node(*element_attrs(info)) for info in data[2:]]
    elements = {node.name: node for node in element_list}
    TABLE = {"L": "left", "R": "right"}
    steps = [TABLE[move] for move in data[0]]

    # Create a NavigationMap object
    map = NavigationMap(elements, steps)

    # Define the starting points for part one and part two
    names_p1 = [elements["AAA"].name]
    names_p2 = [name for name in elements.keys() if name[-1] == "A"]

    print(f"Part 1: {result(map, names_p1, True)}")  # 14681
    print(f"Part 2: {result(map, names_p2, False)}")  # 14321394058031
