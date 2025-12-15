import pytest
from day03.solution import solve_part1, solve_part2
from utils.helpers import read_input

def test_part1_example():
    data = read_input("day03/input_example.txt")
    # Erwartet: 98 + 89 + 78 + 92 = 357
    assert solve_part1(data) == 357

def test_part2_example():
    data = read_input("day03/input_example.txt")
    # Erwartet: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619
    assert solve_part2(data) == 3121910778619
