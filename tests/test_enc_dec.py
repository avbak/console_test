import pytest
from funcs import bin_runner


@pytest.mark.parametrize(
    "operation, text, key, expected",
    [
        ("--encrypt", "Hello", "123", "79575f5d5d"),
        ("--decrypt", "79575f5d5d", "123", "Hello"),
        ("--encrypt", "A", "123", "70"),
        ("--decrypt", "70", "123", "A"),
    ],
)
def test_enc_dec(operation, text, key, expected):
    output = bin_runner([operation, str(text), str(key)])
    assert (
        expected in output
    ), f"Получено значение '{output}' при ожидаемом '{expected}'"


@pytest.mark.parametrize(
    "operation, text, key, expected", [("--encrypt", "HELLO", "HELLO", "0000000000")]
)
def test_check_AES(operation, text, key, expected):
    output = bin_runner([operation, str(text), str(key)])
    assert expected not in output, f"Получено некорретное для AES значение '{output}'"
