def parse_ranges(lines: list[str]) -> list[tuple[int, int]]:
    """
    Parst eine Liste von Zeilen mit Komma-separierten Bereichen zu einer Liste von (start, end)-Tupeln.

    Args:
        lines (list[str]): Zeilen mit Bereichsangaben (z.B. "3-5,10-14").

    Returns:
        list[tuple[int, int]]: Liste der Bereiche als (start, end)-Tupel.
    """
    line = "".join(l.strip() for l in lines)
    ranges = line.split(",")
    result = []
    for r in ranges:
        if not r:
            continue
        start_s, end_s = r.split("-")
        result.append((int(start_s), int(end_s)))
    return result

def read_input(file_path: str) -> list[str]:
    """
    Liest eine Eingabedatei zeilenweise ein und entfernt führende/abschließende Leerzeichen.

    Args:
        file_path (str): Pfad zur Eingabedatei.

    Returns:
        list[str]: Liste der bereinigten Zeilen.
    """
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]
