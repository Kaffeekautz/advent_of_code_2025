def parse_ranges(lines: list[str]) -> list[tuple[int, int]]:
    """Parst eine Liste von Zeilen mit Komma-separierten Ranges zu einer Liste von (start, end)-Tupeln."""
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
    """Liest Input-Datei zeilenweise ein und entfernt Leerzeichen"""
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]
