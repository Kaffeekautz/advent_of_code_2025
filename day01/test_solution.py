from pathlib import Path
from day01.solution import solve_part1, solve_part2, read_input

BASE = Path(__file__).parent


def test_part1_example():
    data = read_input(BASE / "input_example.txt")
    assert solve_part1(data) == 3    # Wert aus dem offiziellen Beispiel


def test_part2_example():
    data = read_input(BASE / "input_example.txt")
    assert solve_part2(data) == 6    # Beispielwert aus Teil 2
