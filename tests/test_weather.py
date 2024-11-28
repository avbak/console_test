import pytest
from funcs import bin_runner
from funcs import dubai_weather


@pytest.mark.parametrize(
    "operation, str1, expected",
    [
          ("--weather", "Abakan", "Current weather"),
          ("--weather", "1", "Weather data not available."),
          ("--weather", "Dubai", dubai_weather())
    ],
)
def test_weather_one_arg(operation, str1, expected):
    output = bin_runner([operation, str1])
    assert (
        expected in output
    ), f"Получено значение '{output}' при ожидаемом '{expected}'"


@pytest.mark.parametrize(
    "operation, str1, str2, expected",
    [
        ("--weather", "--weather", "--weather", "Incorrect input"),
        ("--weather", "Moscow", "FAKEKEY", "Weather data not available."),
        ("--weather", "Moscow", "0ac16edc9db7426a9e442714241211&q=Dubai", dubai_weather())
    ],
)
def test_weather_two_args(operation, str1, str2, expected):
    output = bin_runner([operation, str1, str2])
    assert (
        expected in output
    ), f"Получено значение '{output}' при ожидаемом '{expected}'"
