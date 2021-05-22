from freezegun import freeze_time
from app import get_current_date


@freeze_time("1983-07-06")
def test_get_current_date():
    year, month, day = get_current_date()

    assert year == 1983
    assert month == 7
    assert day == 6
