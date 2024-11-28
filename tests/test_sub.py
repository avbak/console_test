import pytest
from funcs import bin_runner


@pytest.mark.parametrize(
    "operation, int1, int2, expected",
    [
        ("--subtract", 30, 5, "25"),
        ("--subtract", 0, 0, "0"),
        ("--subtract", -5, -10, "5"),
    ],
)
def test_sub(operation, int1, int2, expected):
    output = bin_runner([operation, str(int1), str(int2)])
    assert (
        expected in output
    ), f"Получено значение '{output}' при ожидаемом '{expected}'"
