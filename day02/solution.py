


from utils.helpers import parse_ranges

# =====================
# Part 1: Simple Invalid IDs
# =====================
def is_invalid_id(n: int) -> bool:
    """
    Eine ID ist ungültig, wenn sie eine gerade Länge hat und die erste Hälfte gleich der zweiten Hälfte ist.
    Beispiel: 6464, 123123
    """
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]

def sum_invalid_ids_from_ranges(lines: list[str]) -> int:
    """
    Summiert alle IDs aus den gegebenen Ranges, die nach Part 1 ungültig sind.
    """
    total = 0
    for start, end in parse_ranges(lines):
        for value in range(start, end + 1):
            if is_invalid_id(value):
                total += value
    return total

# =====================
# Part 2: Erweiterte Invalid-IDs (Wiederholungsmuster)
# =====================
def is_invalid_id_extended(n: int) -> bool:
    """
    Eine ID ist ungültig, wenn sie aus einem sich wiederholenden Muster besteht,
    das mindestens zweimal vorkommt (z.B. 1212, 123123, 77, 4444).
    """
    s = str(n)
    length = len(s)
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
    Summiert alle IDs aus den gegebenen Ranges, die nach Part 2 ungültig sind.
    """
    total = 0
    for start, end in parse_ranges(lines):
        for value in range(start, end + 1):
            if is_invalid_id_extended(value):
                total += value
    return total

# =====================
# Hilfsfunktionen & CLI
# =====================
def read_input(path):
    with open(path) as f:
        return f.readlines()

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "example":
        path = "day02/input_example.txt"
    else:
        path = "day02/input.txt"
    lines = read_input(path)
    print("=== Day 02 ===")
    print("Part 1:", sum_invalid_ids_from_ranges(lines))
    print("Part 2:", sum_invalid_ids_from_ranges_part2(lines))

if __name__ == "__main__":
    main()
