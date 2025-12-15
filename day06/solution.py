from utils.helpers import read_input

def solve_part1(data):
    """
    Summiert die Längen aller Zeilen der Eingabe.

    Args:
        data (list[str]): Zeilen der Eingabedatei.

    Returns:
        int: Gesamtsumme der Zeilenlängen.
    """
    return sum(len(line) for line in data)

def solve_part2(data):
    """
    Gibt die maximale Zeilenlänge der Eingabe zurück.

    Args:
        data (list[str]): Zeilen der Eingabedatei.

    Returns:
        int: Maximale Zeilenlänge oder 0 bei leerer Eingabe.
    """
    if not data:
        return 0
    return max(len(line) for line in data)

if __name__ == "__main__":
    data = read_input("day06/input.txt")
    print("Teil 1:", solve_part1(data))
    print("Teil 2:", solve_part2(data))
