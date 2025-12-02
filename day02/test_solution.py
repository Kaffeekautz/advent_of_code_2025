from day02.part1 import sum_invalid_ids_from_ranges, is_invalid_id


def test_is_invalid_id_basic():
    assert is_invalid_id(11)
    assert is_invalid_id(22)
    assert is_invalid_id(99)
    assert is_invalid_id(6464)
    assert is_invalid_id(123123)

    # Ungültige Fälle
    assert not is_invalid_id(101)
    assert not is_invalid_id(123456)
    assert not is_invalid_id(5)


def test_example_input():
    with open("day02/input_example.txt") as f:
        lines = f.readlines()

    result = sum_invalid_ids_from_ranges(lines)

    assert result == 1227775554
