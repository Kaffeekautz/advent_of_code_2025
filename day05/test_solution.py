
import pytest
from day05.solution import solve_part1, solve_part2
from utils.helpers import read_input

def test_part1_example():
    """
    Testet Teil 1 anhand des Beispiels aus der Aufgabenstellung.
    """
    example = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]
    assert solve_part1(example) == 3

def test_part2_example():
    """
    Testet Teil 2 (Platzhalter) mit Beispieldaten.
    """
    data = read_input("day05/input_example.txt")
    assert solve_part2(data) == max(len(line) for line in data)
