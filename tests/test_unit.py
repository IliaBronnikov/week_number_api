from datetime import date

from services import week_number
import pytest


@pytest.mark.parametrize(
    ("dt", "expected"),
    [
        (date(2019, 1, 5), 1),  # saturday - 6
        (date(2019, 1, 6), 2),  # sunday - 0
        (date(2021, 1, 3), 2),  # sunday - 0
        (date(2021, 1, 2), 1),  # saturday - 6
        (date(2021, 1, 10), 3),  # sunday - 0
        (date(2011, 1, 1), 1),  # saturday - 6
        (date(2011, 1, 2), 2),  # sunday - 0
        (date(2011, 1, 4), 2),  # tuesday - 2
    ],
)
def test_week_number(dt, expected):
    assert week_number(dt) == expected
