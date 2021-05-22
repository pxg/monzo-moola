import datetime
import os
from pprint import pprint

import requests


def get_current_date():
    now = datetime.datetime.now()
    return now.year, now.month, now.day


def get_current_account_balance(account_id, access_token):
    """
    Get current account balance in pence from Monzo
    """
    response = requests.get(
        f"https://api.monzo.com/balance?account_id={account_id}",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    return response.json()["balance"]


def write_to_google_sheets(balance):
    pass


def get_pots_data(account_id, access_token):
    response = requests.get(
        f"https://api.monzo.com/pots?current_account_id={account_id}",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    return response.json()


def get_savings_stash_balance(account_id, access_token):
    pots = get_pots_data(account_id, access_token)["pots"]
    savings_stash_pot_id = "pot_00009dUcQOPx5aOmh6mQPB"
    return next(pot["balance"] for pot in pots if pot["id"] == savings_stash_pot_id)


if __name__ == "__main__":
    data = get_pots_data(
        account_id=os.environ.get("MONZO_ACCOUNT_ID"),
        access_token=os.environ.get("MONZO_ACCESS_TOKEN"),
    )
    pprint(data)
