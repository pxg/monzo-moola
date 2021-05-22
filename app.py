import datetime
import os
from pprint import pprint

import requests


def get_balance_api_url(account_id):
    """
    Get Balance URL for Monzo API
    """
    # TODO: update to https://api.monzo.com/balance
    return "https://api.getmondo.co.uk/balance?account_id={}".format(account_id)


def get_current_date():
    now = datetime.datetime.now()
    return now.year, now.month, now.day


def get_current_balance(account_id, access_token):
    """
    Get current account balance in pence from Monzo
    """
    response = requests.get(
        get_balance_api_url(account_id),
        headers={"Authorization": "Bearer {}".format(access_token)},
    )
    return response.json()["balance"]


def write_to_google_sheets(balance):
    pass


def get_pots_data(account_id, access_token):
    response = requests.get(
        "https://api.monzo.com/pots?current_account_id={}".format(account_id),
        headers={"Authorization": "Bearer {}".format(access_token)},
    )
    return response.json()


def get_savings_stash_balance(account_id, access_token):
    response = get_pots_data(account_id, access_token)
    # TODO: alternative to for loop?
    for pot in response["pots"]:
        if pot["id"] == "pot_00009dUcQOPx5aOmh6mQPB":
            return pot["balance"]


if __name__ == "__main__":
    data = get_pots_data(
        account_id=os.environ.get("MONZO_ACCOUNT_ID"),
        access_token=os.environ.get("MONZO_ACCESS_TOKEN"),
    )
    pprint(data)
