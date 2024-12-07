# Advent of Code 2023
# Day 2: Conundrum

from dataclasses import dataclass
from typing import Self

import numpy as np
from numpy.typing import NDArray


def game_attrs(info: str) -> tuple[int, NDArray]:
    """Extract the game id and rolls matrix from a string.
    An example of a possible string is in the form:
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green".
    Rolls matrix has a row for each roll, and the columns
    are, respectively, the number of red, green and blue"""

    id_info, rolls_info = info.split(":")
    _, id = id_info.split(" ")
    records = rolls_info.split(";")

    rolls = np.zeros((len(records), 3), dtype=int)
    for i, record in enumerate(records):
        record = record.split(",")
        counts = {"red": 0, "green": 0, "blue": 0}
        for dice in record:
            _, num, color = dice.split(" ")
            counts[color] = int(num)
        rolls[i,] = list(counts.values())

    return int(id), rolls


@dataclass
class Game:
    id: int
    rolls: NDArray

    @classmethod
    def from_string(cls, string: str) -> Self:
        return cls(*game_attrs(string))

    @property
    def max_rolls(self) -> NDArray:
        return self.rolls.max(axis=0)

    @property
    def power(self) -> int:
        return self.max_rolls.prod()

    def is_possible(self, limits=[12, 13, 14]) -> bool:
        return all(self.max_rolls <= limits)


if __name__ == "__main__":

    def result_p1(games: list[Game]) -> int:
        possible_ids = [game.id for game in games if game.is_possible()]
        return sum(possible_ids)

    def result_p2(games: list[Game]) -> int:
        games_powers = [game.power for game in games]
        return sum(games_powers)

    with open("data/2_conundrum.txt", "r") as file:
        data = file.read().splitlines()
        games = [Game.from_string(line) for line in data]

    print(f"Part one answer: {result_p1(games)}")  # 2439
    print(f"Part two answer: {result_p2(games)}")  # 63711
