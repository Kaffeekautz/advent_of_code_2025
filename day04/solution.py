
"""
Day 4: Printing Department
-------------------------
Dieses Skript löst das Advent of Code 2025, Tag 4, Teil 1.

Gegeben ist ein Gitter, das Papierrollen ('@') und leere Felder ('.') enthält. Eine Papierrolle ist für einen Gabelstapler zugänglich, wenn weniger als vier benachbarte Felder (horizontal, vertikal oder diagonal) ebenfalls eine Papierrolle enthalten.

Dieses Skript zählt alle zugänglichen Papierrollen im Gitter.

Funktionen:
- solve_part1: Zählt die zugänglichen Papierrollen gemäß der oben beschriebenen Regel.
- solve_part2: Platzhalter für Teil 2 (aktuell: maximale Zeilenlänge).

Eingabe: day04/input.txt
Ausgabe: Anzahl der zugänglichen Papierrollen (Part 1)
"""

from utils.helpers import read_input

def solve_part1(data):
    """
    Ermittelt die Anzahl der zugänglichen Papierrollen im Gitter.

    Eine Papierrolle ('@') ist zugänglich, wenn sie weniger als vier benachbarte Papierrollen hat.
    Benachbart sind alle acht Felder um eine Zelle (horizontal, vertikal, diagonal).

    Args:
        data (list[str]): Das Gitter als Liste von Strings.

    Returns:
        int: Anzahl der zugänglichen Papierrollen.
    """
    rows = len(data)
    cols = len(data[0]) if data else 0
    accessible = 0
    for r in range(rows):
        for c in range(cols):
            if data[r][c] != '@':
                continue
            # Zähle benachbarte Papierrollen
            neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue  # eigene Zelle überspringen
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if data[nr][nc] == '@':
                            neighbors += 1
            if neighbors < 4:
                accessible += 1
    return accessible

def solve_part2(data):
    """
    Simuliert das wiederholte Entfernen aller zugänglichen Papierrollen.
    Eine Papierrolle ist zugänglich, wenn sie weniger als vier benachbarte Papierrollen hat.
    Nach jedem Entfernen wird das Gitter aktualisiert und der Vorgang wiederholt,
    bis keine Papierrolle mehr entfernt werden kann.

    Args:
        data (list[str]): Das Gitter als Liste von Strings.

    Returns:
        int: Gesamtzahl der entfernten Papierrollen.
    """
    from copy import deepcopy

    grid = [list(row) for row in data]
    rows = len(grid)
    cols = len(grid[0]) if grid else 0
    total_removed = 0

    while True:
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '@':
                    continue
                neighbors = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '@':
                                neighbors += 1
                if neighbors < 4:
                    to_remove.append((r, c))
        if not to_remove:
            break
        for r, c in to_remove:
            grid[r][c] = '.'
        total_removed += len(to_remove)
    return total_removed

if __name__ == "__main__":
    data = read_input("day04/input.txt")
    print("Part 1 (zugängliche Papierrollen):", solve_part1(data))
    print("Part 2 (Platzhalter):", solve_part2(data))
