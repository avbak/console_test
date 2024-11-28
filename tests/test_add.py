import pytest
from funcs import bin_runner


@pytest.mark.parametrize(
    "operation, int1, int2, expected",
    [("--add", 3, 5, "8"), ("--add", 0, 0, "0"), ("--add", -5, -10, "-15")],
)
def test_add(operation, int1, int2, expected):
    output = bin_runner([operation, str(int1), str(int2)])
    assert (
        expected in output
    ), f"Получено значение '{output}' при ожидаемом '{expected}'"
