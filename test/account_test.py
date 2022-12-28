import pytest

from src.token_erc20 import Token
from src.deploy import *
from src.local_addresses import *

mint_amount = 100
fund_amount = 100


@pytest.fixture
def token():

    addresses["token_local_address"] = deploy_token().address

    return Token(w3.eth.default_account, 1337, "http://localhost:8545")


def testing(token):

    token.mint(mint_amount)

    token.set_fund_amount(fund_amount)

    token.fund_account()

    print(token.fetch_balance_of(w3.eth.default_account))
