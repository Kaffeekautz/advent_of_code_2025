from utils.helpers import read_input

def solve_part1(data):
    """Beispiel: Summe der Längen aller Zeilen"""
    return sum(len(line) for line in data)

def solve_part2(data):
    """Beispiel: Maximale Zeilenlänge"""
    if not data:
        return 0
    return max(len(line) for line in data)

if __name__ == "__main__":
    data = read_input("day06/input.txt")
    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))
