# Advent of Code 2023
# Day 4: Scratchcards

from dataclasses import dataclass
from typing import Self

import numpy as np
from numpy.typing import NDArray


def card_attrs(info: str) -> tuple[int, list[int], list[int]]:
    """Extract the card id, winning numbers and losing numbers
    from a string. An example of a possible string is in the
    form: "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"."""

    id_info, nums_info = info.split(":")
    *_, id = id_info.split(" ")
    wnums, lnums = nums_info.split("|")
    wnums = [int(x) for x in wnums.split()]
    lnums = [int(x) for x in lnums.split()]

    return int(id), wnums, lnums


@dataclass
class Scratchcard:
    id: int
    wnums: list[int]
    lnums: list[int]

    @classmethod
    def from_string(cls, string: str) -> Self:
        return cls(*card_attrs(string))

    @property
    def nhits(self) -> int:
        return np.isin(self.wnums, self.lnums).sum()

    @property
    def points(self) -> int:
        return 2 ** max(self.nhits - 1, 0)

    @property
    def awards(self) -> NDArray:
        return np.arange(self.id, self.id + self.nhits)


if __name__ == "__main__":

    def result_p1(cards: list[Scratchcard]) -> int:
        points = [card.points for card in cards]
        return sum(points)

    def result_p2(cards: list[Scratchcard]) -> int:
        counts = np.full_like(cards, 1)
        for card in cards:
            indices = card.awards[: len(cards)]
            counts[indices] += counts[card.id - 1]
        return sum(counts)

    with open("data/4_scratchcards.txt", "r") as file:
        data = file.read().splitlines()
        cards = [Scratchcard.from_string(line) for line in data]

    print(f"Part one answer: {result_p1(cards)}")  # 21105
    print(f"Part two answer: {result_p2(cards)}")  # 5329815
