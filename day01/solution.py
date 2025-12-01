
from pathlib import Path


def read_input(path):
    """
    Liest die Eingabedatei ein und gibt eine Liste mit den Zeilen zurück.
    Erwartet eine Pfadangabe (Path oder str).
    """
    path = Path(path)
    return [line.strip() for line in path.read_text().splitlines()]


# ---------------------------------------------------------------------------
# Teil 1
# ---------------------------------------------------------------------------

def solve_part1(data):
    """
    Ermittelt, wie oft der Zeiger am Ende einer Rotation auf 0 landet.
    Startposition ist immer 50.
    """

    position = 50
    count_zeros = 0

    for line in data:
        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            position = (position - distance) % 100
        else:  # direction == "R"
            position = (position + distance) % 100

        if position == 0:
            count_zeros += 1

    return count_zeros


# ---------------------------------------------------------------------------
# Teil 2
# ---------------------------------------------------------------------------

def solve_part2(data):
    """
    Zählt, wie oft der Zeiger *während* einer Rotation oder am Ende davon auf 0 zeigt.
    Jeder einzelne Klick wird berücksichtigt.
    """

    position = 50
    count_zeros = 0

    for line in data:
        direction = line[0]
        distance = int(line[1:])

        # Schrittweite abhängig von Richtung
        step = -1 if direction == "L" else 1

        # Jede einzelne Bewegung durchlaufen
        for _ in range(distance):
            position = (position + step) % 100
            if position == 0:
                count_zeros += 1

    return count_zeros


if __name__ == "__main__":
    # Datei einlesen
    data = read_input("day01/input.txt")  # dein Puzzle-Input

    # Part 1 ausführen und ausgeben
    result_part1 = solve_part1(data)
    print("Part 1 Lösung:", result_part1)

    # Part 2 ausführen und ausgeben
    result_part2 = solve_part2(data)
    print("Part 2 Lösung:", result_part2)
