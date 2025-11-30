import pytest
from day01.solution import solve_part1, solve_part2
from utils.helpers import read_input

def test_part1_example():
    data = read_input("day01/input_example.txt")
    assert solve_part1(data) == sum(len(line) for line in data)

def test_part2_example():
    data = read_input("day01/input_example.txt")
    assert solve_part2(data) == max(len(line) for line in data)
