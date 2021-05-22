import os

from pytest import fixture, mark
from freezegun import freeze_time

from app import (
    get_current_date,
    get_current_account_balance,
    get_savings_stash_balance,
)


@fixture
def account_id():
    return os.environ.get("MONZO_ACCOUNT_ID")


@fixture
def access_token():
    return os.environ.get("MONZO_ACCESS_TOKEN")


@freeze_time("1983-07-06")
def test_get_current_date():
    year, month, day = get_current_date()

    assert year == 1983
    assert month == 7
    assert day == 6


@mark.live_api
def test_get_current_account_balance(account_id, access_token):
    account_id = os.environ.get("MONZO_ACCOUNT_ID")
    access_token = os.environ.get("MONZO_ACCESS_TOKEN")

    balance = get_current_account_balance(account_id, access_token)

    assert isinstance(balance, int) is True


@mark.live_api
def test_get_savings_stash_balance(account_id, access_token):
    balance = get_savings_stash_balance(account_id, access_token)

    assert isinstance(balance, int) is True
