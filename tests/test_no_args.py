import pytest
from funcs import bin_runner


@pytest.mark.parametrize("operation, int1, expected", [("--add", 0, "Incorrect input")])
def test_one_of_two_args(operation, int1, expected):
    output = bin_runner([operation, str(int1)])
    assert (
        expected in output
    ), f"Получено значение '{output}' при ожидаемом '{expected}'"


@pytest.mark.parametrize("operation, expected", [("--multiply", "Incorrect input")])
def test_null_of_two_args(operation, expected):
    output = bin_runner([operation])
    assert (
        expected in output
    ), f"Получено значение '{output}' при ожидаемом '{expected}'"
