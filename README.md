# Advent of Code 2025

Dieses Repository enthält meine Lösungen für die Advent of Code 2025 Programmier-Challenge. Für jeden Tag gibt es einen eigenen Ordner mit Beispiel- und Eingabedateien, Lösungscode und Tests.

## Projektstruktur

- `dayXX/` – Ordner für jeden Tag (01–25), jeweils mit:
  - `__init__.py` – macht das Verzeichnis zum Python-Package
  - `solution.py` – deine Lösung für Part 1 und Part 2
  - `test_solution.py` – pytest-Tests für Beispiele
  - `input.txt` – echter Puzzle-Input von AoC
  - `input_example.txt` – Beispielinput aus der Aufgabenstellung
- `utils/` – Hilfsfunktionen, z.B. für das Einlesen von Dateien
- `requirements.txt` – Python-Abhängigkeiten
- `.venv/` – (optional) virtuelle Umgebung

## Setup

1. Virtuelle Umgebung anlegen und aktivieren:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

## Nutzung

- Eigene Lösung ausführen (z.B. für Tag 1):
  ```bash
  python3 day01/solution.py
  ```
- Tests für einen Tag ausführen:
  ```bash
  pytest day01/test_solution.py
  ```
- Alle Tests im Projekt ausführen:
  ```bash
  pytest
  ```

## Eigene Lösungen

- Schreibe deine Lösung in `solution.py` im jeweiligen Tagesordner.
- Die Funktion `read_input` aus `utils/helpers.py` hilft beim Einlesen der Inputdateien.
- Passe die Tests in `test_solution.py` an die Beispiele aus der Aufgabenstellung an.

## Beispiel für eine Lösung (Tag 1)

```python
def solve_part1(data):
    # Beispiel: Zähle, wie oft der Zeiger auf 0 landet
    ...

def solve_part2(data):
    # Beispiel: Zähle, wie oft der Zeiger während der Bewegung auf 0 zeigt
    ...
```

## Hinweise

- Die Inputdateien sind nicht im Repository enthalten, da sie individuell von AoC bereitgestellt werden.
- Die Tests orientieren sich an den offiziellen Beispielen von Advent of Code.
