import pytest
import threading
from funcs import bin_runner
from funcs import get_ram


@pytest.mark.parametrize(
    "operation, int1, expected",
    [
        ("--meaning", 0, "42"),
        ("--meaning", 50, "42"),
        ("--meaning", 50.12345, "42"),
        ("--meaning", 100, "42"),
        ("--meaning", 100.00000000000000000000000000001, "Error"),
        ("--meaning", "a", "Error"),
    ],
)
def test_meaning(operation, int1, expected):
    output = None
    ram = None

    def get_output():
        nonlocal output
        output = bin_runner([operation, str(int1)])

    def get_ram_value():
        nonlocal ram
        ram = get_ram()

    thread_output = threading.Thread(target=get_output)
    thread_ram = threading.Thread(target=get_ram_value)

    thread_output.start()
    thread_ram.start()

    thread_output.join()
    thread_ram.join()

    assert (
        (expected in output) and ("None" not in output) and (ram <= float(1024))
    ), f"Получено значение '{output}/None' при ожидаемом '{expected}', либо превышен лимит ОЗУ (использовано '{ram}'MB)"
