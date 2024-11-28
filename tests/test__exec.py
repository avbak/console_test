import pytest
from funcs import bin_runner


@pytest.mark.parametrize("expected", [("Displays this help message")])
def test_exec(expected):
    output = bin_runner([])
    assert (
        expected in output
    ), f"Получено значение '{output}' при ожидаемом '{expected}'"
