def is_invalid_id_extended(n: int) -> bool:
    """
    Prüft, ob eine ID invalid ist nach den erweiterten Regeln von Part 2.
    Die Zahl ist ungültig, wenn sie aus einem sich wiederholenden Muster besteht,
    welches mindestens zweimal vorkommt.
    """
    s = str(n)
    length = len(s)

    # Muster kann höchstens die Hälfte der Länge haben
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len != 0:
            continue

        pattern = s[:pattern_len]
        repetitions = length // pattern_len

        if s == pattern * repetitions and repetitions >= 2:
            return True

    return False


def sum_invalid_ids_from_ranges_part2(lines: list[str]) -> int:
    """
    Liest die ID-Bereiche ein und summiert alle IDs,
    die nach den Regeln von Part 2 invalid sind.
    """
    line = "".join(l.strip() for l in lines)  # Zeilen zusammenführen
    ranges = line.split(",")

    total = 0
    for r in ranges:
        if not r:
            continue

        start_s, end_s = r.split("-")
        start, end = int(start_s), int(end_s)

        for value in range(start, end + 1):
            if is_invalid_id_extended(value):
                total += value

    return total


def solve_part2():
    with open("day02/input.txt") as f:
        lines = f.readlines()
    result = sum_invalid_ids_from_ranges_part2(lines)
    print(result)
