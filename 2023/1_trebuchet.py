# Advent of Code 2023
# Day 1: Trebuchet


def words_to_numeric(string: str) -> str:
    """Replace digits written as words with numeric digits.
    First and last characters are mantained to avoid problems
    with more than one digit sharing the same character."""

    WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    NUMERICS = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]

    for word, numeric in zip(WORDS, NUMERICS):
        string = string.replace(word, numeric)
    return string


def calibration_value(string: str, as_chars=False) -> int:
    """Calculate the calibration value of a string, which is the
    concatenation of the first and last digits of the string.
    If as_chars is True, digits written as words are considered
    and converted into numeric digits before computation."""

    if as_chars:
        string = words_to_numeric(string)

    digits = [char for char in string if char.isdigit()]
    return int(digits[0] + digits[-1])


if __name__ == "__main__":

    def result(values: list[str], as_chars=False) -> int:
        cvalues = [calibration_value(x, as_chars) for x in values]
        return sum(cvalues)

    with open("data/1_trebuchet.txt", "r") as file:
        data = file.read().splitlines()

    print(f"Part one answer: {result(data)}")  # 54338
    print(f"Part two answer: {result(data, as_chars=True)}")  # 53389
