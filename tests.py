import os

from freezegun import freeze_time
from app import get_current_date, get_current_balance, get_savings_stash_balance


@freeze_time("1983-07-06")
def test_get_current_date():
    year, month, day = get_current_date()

    assert year == 1983
    assert month == 7
    assert day == 6


# TODO: add mark live api
def test_get_current_balance():
    account_id = os.environ.get("MONZO_ACCOUNT_ID")
    access_token = os.environ.get("MONZO_ACCESS_TOKEN")

    balance = get_current_balance(account_id, access_token)

    assert isinstance(balance, int) is True


# TODO: add mark live api
def test_get_savings_stash_balance():
    # TODO: create fixture
    account_id = os.environ.get("MONZO_ACCOUNT_ID")
    access_token = os.environ.get("MONZO_ACCESS_TOKEN")

    balance = get_savings_stash_balance(account_id, access_token)

    assert isinstance(balance, int) is True
