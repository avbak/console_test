import pytest
from funcs import bin_runner


@pytest.mark.parametrize(
    "operation, int1, int2, expected",
    [
        ("--divide", 30, 5, "6"),
        ("--divide", 3, 2, "1"),
        ("--divide", 0, 0, "Error"),
        ("--divide", -100, 0, "Error"),
    ],
)
def test_div(operation, int1, int2, expected):
    output = bin_runner([operation, str(int1), str(int2)])
    assert (
        expected in output
    ), f"Получено значение '{output}' при ожидаемом '{expected}'"
