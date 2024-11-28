import pytest
from funcs import bin_runner


@pytest.mark.parametrize(
    "operation, int1, int2, expected",
    [
        ("--multiply", 5, 5, "25"),
        ("--multiply", 0, 0, "0"),
        ("--multiply", 1000, 1337, "1337000"),
        ("--multiply", 1000, -1337, "-1337000"),
        ("--multiply", -1000, 1337, "-1337000"),
    ],
)
def test_sub(operation, int1, int2, expected):
    output = bin_runner([operation, str(int1), str(int2)])
    assert (
        expected in output
    ), f"Получено значение '{output}' при ожидаемом '{expected}'"
