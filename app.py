import os
import requests

# TODO:
# 1. write test
# 2. add gutted in sublime settings
# 3. write to Google sheets for today


def get_current_balance(account_id, access_token):
    """
    Get current account balance in pence from Monzo
    """
    response = requests.get(
        'https://api.getmondo.co.uk/balance?account_id={}'.format(account_id),
        headers={'Authorization': 'Bearer {}'.format(access_token)})
    return response.json()['balance']


balance = get_current_balance(
    account_id='acc_00009HcwLElM5mpuV0vxwn',
    access_token=os.environ.get('MONZO_ACCESS_TOKEN'))
print('balance in pence {}'.format(balance))
