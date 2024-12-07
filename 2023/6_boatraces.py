# Advent of Code 2023
# Day 6: Boat Races

from dataclasses import dataclass

import numpy as np


def race_attrs(data: list[str]):
    _, time = data[0].split(":")
    _, dist = data[1].split(":")
    time = [int(x) for x in time.split()]
    dist = [int(x) for x in dist.split()]
    return zip(time, dist)


@dataclass
class BoatRace:
    time: int
    dist: int

    @property
    def value(self) -> int:
        """Given a time (T>0) and distance (D>=T/2), compute
        the smallest integer such that: n * (T - n) > D."""

        roots = np.roots([1, -self.time, self.dist + 1])
        return np.ceil(roots.min()).astype(int)

    @property
    def wins(self) -> int:
        return self.time + 1 - 2 * self.value


if __name__ == "__main__":

    def result(races: list[BoatRace]) -> np.int_:
        return np.prod([br.wins for br in races])

    with open("data/6_toyboatraces.txt", "r") as file:
        data = file.read().splitlines()
        races = [BoatRace(t, d) for t, d in race_attrs(data)]
        final_race = BoatRace(44899691, 277113618901768)

    print(f"Part one answer: {result(races)}")  # 2344708
    print(f"Part two answer: {final_race.wins}")  # 30125202
