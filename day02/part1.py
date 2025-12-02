def is_invalid_id(n: int) -> bool:
    s = str(n)

    # Länge muss gerade sein
    if len(s) % 2 != 0:
        return False

    half = len(s) // 2
    return s[:half] == s[half:]


def sum_invalid_ids_from_ranges(lines: list[str]) -> int:
    line = "".join(l.strip() for l in lines)  # Zeilen zusammenführen
    ranges = line.split(",")

    total = 0
    for r in ranges:
        if not r:
            continue

        start_s, end_s = r.split("-")
        start, end = int(start_s), int(end_s)

        for value in range(start, end + 1):
            if is_invalid_id(value):
                total += value

    return total


def solve_part1():
    with open("day02/input.txt") as f:
        lines = f.readlines()
    result = sum_invalid_ids_from_ranges(lines)
    print(result)


if __name__ == "__main__":
    solve_part1()
