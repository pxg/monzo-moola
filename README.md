# Monzo Moola

## Installation
```
pip install -r requirements.txt
```

You'll need to set environment variables for:
- MONZO_ACCOUNT_ID
- MONZO_ACCESS_TOKEN
The values for these can be found on https://developers.monzo.com/api/playground.

It's recommended you use https://direnv.net/ and a `.envrc` file to do this.

## Running the tests
```
py.test tests.py
```

To run the tests without hitting the live api:
```
py.test -m "not live_api" tests.py
```