from utils.helpers import read_input

def solve_part1(data):
    """
    Für jede Zeile finde die größte zweistellige Zahl, indem du zwei Ziffern in Reihenfolge auswählst (nicht notwendigerweise benachbart).
    Summiere diese Zahlen.
    """
    from itertools import combinations
    total = 0
    for line in data:
        n = len(line)
        max_joltage = 0
        for idxs in combinations(range(n), 2):
            num = int(line[idxs[0]] + line[idxs[1]])
            if num > max_joltage:
                max_joltage = num
        total += max_joltage
    return total

def solve_part2(data):
    """
    Für jede Zeile finde die größte mögliche 12-stellige Zahl, indem du 12 Ziffern in Reihenfolge auswählst (nicht notwendigerweise benachbart).
    Summiere diese Zahlen.
    """
    total = 0
    k = 12
    for line in data:
        n = len(line)
        result = []
        start = 0
        for to_pick in range(k, 0, -1):
            # Suchbereich: von start bis n - to_pick
            max_digit = '0'
            max_idx = -1
            for i in range(start, n - to_pick + 1):
                if line[i] > max_digit:
                    max_digit = line[i]
                    max_idx = i
            result.append(max_digit)
            start = max_idx + 1
        num = int(''.join(result))
        total += num
    return total

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "example":
        data = read_input("day03/input_example.txt")
    else:
        data = read_input("day03/input.txt")
    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))
