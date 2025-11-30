def read_input(file_path: str) -> list[str]:
    """Liest Input-Datei zeilenweise ein und entfernt Leerzeichen"""
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]
