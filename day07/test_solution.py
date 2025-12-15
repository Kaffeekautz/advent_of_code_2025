import pytest
from day07.solution import solve_part1, solve_part2
from utils.helpers import read_input

def test_part1_example():
    """
    Testet Teil 1 mit Beispieldaten: Erwartet die Summe der Längen aller Zeilen.
    """
    data = read_input("day07/input_example.txt")
    assert solve_part1(data) == sum(len(line) for line in data)

def test_part2_example():
    """
    Testet Teil 2 mit Beispieldaten: Erwartet die maximale Zeilenlänge.
    """
    data = read_input("day07/input_example.txt")
    assert solve_part2(data) == max(len(line) for line in data)
