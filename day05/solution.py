
from utils.helpers import read_input

def solve_part1(data):
    """
    Bestimmt die Anzahl der frischen Zutaten-IDs.

    Eine Zutat ist frisch, wenn ihre ID in mindestens einem der angegebenen Bereiche liegt.
    Die Eingabe besteht aus zwei Abschnitten, getrennt durch eine Leerzeile:
    - Bereichsangaben (z.B. "3-5")
    - Verfügbare IDs (eine pro Zeile)

    Args:
        data (list[str]): Zeilen der Eingabedatei.

    Returns:
        int: Anzahl der frischen IDs.
    """
    # Eingabe in Bereiche und IDs aufteilen
    if not data:
        return 0
    try:
        blank_idx = data.index("")
    except ValueError:
        return 0  # Keine Leerzeile, ungültige Eingabe
    range_lines = data[:blank_idx]
    id_lines = data[blank_idx+1:]
    # Bereiche parsen
    ranges = []
    for line in range_lines:
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
    # IDs parsen
    ids = [int(line) for line in id_lines if line.strip().isdigit()]
    # Prüfen, welche IDs frisch sind
    fresh_count = 0
    for id_ in ids:
        if any(start <= id_ <= end for (start, end) in ranges):
            fresh_count += 1
    return fresh_count

def solve_part2(data):
    """
    Bestimmt die Anzahl aller eindeutigen IDs, die in mindestens einem Bereich liegen.
    Die zweite Sektion (IDs) wird ignoriert.

    Args:
        data (list[str]): Zeilen der Eingabedatei.

    Returns:
        int: Anzahl der als frisch geltenden IDs laut Bereichsangaben.
    """
    if not data:
        return 0
    try:
        blank_idx = data.index("")
    except ValueError:
        blank_idx = len(data)  # Falls keine Leerzeile, alles als Bereich nehmen
    range_lines = data[:blank_idx]
    # Bereiche parsen und alle IDs sammeln
    fresh_ids = set()
    for line in range_lines:
        if "-" in line:
            start, end = map(int, line.split("-"))
            fresh_ids.update(range(start, end + 1))
    return len(fresh_ids)

if __name__ == "__main__":
    data = read_input("day05/input.txt")
    print("Teil 1:", solve_part1(data))
    print("Teil 2:", solve_part2(data))
