import pytest
from day04.solution import solve_part1, solve_part2
from utils.helpers import read_input

def test_part1_example():
    data = read_input("day04/input_example.txt")
    # Erwartet: 13 zugängliche Rollen im Beispiel
    assert solve_part1(data) == 13

def test_part2_example():
    data = read_input("day04/input_example.txt")
    # Erwartet: 43 Rollen können insgesamt entfernt werden
    assert solve_part2(data) == 43
